import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

COLOR_BG       = "#111820"   
COLOR_PANEL    = "#1a2029"   
COLOR_PRIMARY  = "#e82631"   
COLOR_GREEN    = "#32b36b"
COLOR_BLUE     = "#4aa3ff"
COLOR_ORANGE   = "#ff8c00"   
COLOR_BTN      = "#2a2f38"
COLOR_TEXT     = "#e9eef2"
COLOR_TICKET_BG = "#ffffff"
COLOR_TICKET_TXT = "#222222"

root = tk.Tk()
root.title("Login")
root.geometry("320x260")

user_var = tk.StringVar()
pass_var = tk.StringVar()

tk.Label(root, text="Usuario").pack(pady=(12,2))
tk.Entry(root, textvariable=user_var).pack(pady=(0,8), padx=12)

tk.Label(root, text="Contraseña").pack(pady=(8,2))
tk.Entry(root, show="*", textvariable=pass_var).pack(pady=(0,12), padx=12)

def abrir_pos():
    root.withdraw()

    pos = tk.Toplevel(root)
    pos.title("POS")
    pos.state("zoomed")
    pos.configure(bg=COLOR_BG)

    pos.grid_columnconfigure(0, weight=0)
    pos.grid_columnconfigure(1, weight=1)
    pos.grid_columnconfigure(2, weight=0)
    pos.grid_rowconfigure(1, weight=1)

    precios = {
        "Simple": 8000.00,
        "Doble": 15000.00,
        "Triple": 20000.00,
        "Dip Cheddar": 1200.00,       
        "Porción de Papas": 3000.00,
        "Promo2x1": 19500,
        "Clasica simple":8000.00,
        "Clasica doble":15000.00,
        "Clasica triple": 20000.00
    }

    items = {}
    total_var = tk.DoubleVar(value=0.0)
    selected_item_var = tk.StringVar(value="")

    line_to_item = {}

    def actualizar_total_label():
        barra_total.config(text=f"  Ttl {total_var.get():.2f}")

    def render_ticket():
        ticket.config(state="normal")
        ticket.delete("1.0", "end")
        line_to_item.clear()
        total = 0.0
        line_no = 1
        for nombre, qty in items.items():
            pu = precios.get(nombre, 0.0)
            sub = pu * qty
            total += sub
            ticket.insert("end", f"{qty} x {nombre:<18}{sub:>12.2f}\n")
            line_to_item[line_no] = nombre
            line_no += 1
        ticket.config(state="disabled")
        total_var.set(total)
        actualizar_total_label()
        resaltar_seleccion()

    def limpiar_pedido():
        items.clear()
        selected_item_var.set("")
        render_ticket()

    def on_product_click(nombre):
        items[nombre] = items.get(nombre, 0) + 1
        selected_item_var.set(nombre)
        render_ticket()

    def seleccionar_por_linea(line_no):
        nombre = line_to_item.get(line_no, "")
        if nombre:
            selected_item_var.set(nombre)
            resaltar_seleccion()

    def resaltar_seleccion():
        ticket.config(state="normal")
        ticket.tag_delete("selitem")
        ticket.tag_configure("selitem", background="#ffe9e9")
        nombre_sel = selected_item_var.get()
        if not nombre_sel:
            ticket.config(state="disabled")
            return
        for ln, nm in line_to_item.items():
            if nm == nombre_sel:
                start = f"{ln}.0"
                end = f"{ln}.end"
                ticket.tag_add("selitem", start, end)
        ticket.config(state="disabled")

    def borrar_uno():
        n = selected_item_var.get()
        if not n:
            return
        if n in items:
            items[n] -= 1
            if items[n] <= 0:
                del items[n]
                selected_item_var.set("")
            render_ticket()

    def logout():
        pos.destroy()
        user_var.set("")
        pass_var.set("")
        root.deiconify()

    def cobrar():
        if total_var.get() <= 0:
            messagebox.showinfo("Cobrar", "No hay ítems en el pedido.")
            return

        pay = tk.Toplevel(pos)
        pay.title("Cobrar")
        pay.transient(pos)
        pay.grab_set()
        pay.resizable(False, False)

        tk.Label(pay, text=f"Total a cobrar: $ {total_var.get():.2f}",
                 font=("Segoe UI", 12, "bold")).grid(row=0, column=0, columnspan=2, padx=16, pady=(16,8), sticky="w")

        tk.Label(pay, text="Efectivo recibido:").grid(row=1, column=0, padx=(16,6), pady=6, sticky="e")
        monto_var = tk.StringVar(value="")
        entry = tk.Entry(pay, textvariable=monto_var, justify="right", font=("Segoe UI", 14), width=12)
        entry.grid(row=1, column=1, padx=(6,16), pady=6, sticky="w")

        tk.Label(pay, text="Vuelto:").grid(row=2, column=0, padx=(16,6), pady=(6,12), sticky="e")
        vuelto_var = tk.StringVar(value="$ 0.00")
        tk.Label(pay, textvariable=vuelto_var, font=("Segoe UI", 12, "bold")).grid(row=2, column=1, padx=(6,16), pady=(6,12), sticky="w")

        btns = tk.Frame(pay); btns.grid(row=3, column=0, columnspan=2, pady=(4,16))
        btn_ok = tk.Button(btns, text="Efectivizar", state="disabled",
                           bg=COLOR_GREEN, fg="white", relief="flat",
                           padx=14, pady=8)
        btn_ok.grid(row=0, column=0, padx=6)
        tk.Button(btns, text="Cancelar", command=pay.destroy,
                  relief="flat", padx=14, pady=8).grid(row=0, column=1, padx=6)

        def parse_monto(s):
            try:
                return float(s.replace(",", "."))
            except Exception:
                return None

        def on_change(*_):
            m = parse_monto(monto_var.get())
            if m is None:
                btn_ok.config(state="disabled")
                vuelto_var.set("$ 0.00")
                return
            change = m - total_var.get()
            btn_ok.config(state=("normal" if change >= 0 else "disabled"))
            vuelto_var.set(f"$ {max(change, 0):.2f}")

        def efectivizar():
            m = parse_monto(monto_var.get()) or 0.0
            change = m - total_var.get()
            if change < 0:
                return
            messagebox.showinfo(
                "Venta realizada",
                f"Pago:   $ {m:.2f}\nTotal:  $ {total_var.get():.2f}\nVuelto: $ {change:.2f}"
            )
            pay.destroy()
            limpiar_pedido()

        monto_var.trace_add("write", on_change)
        btn_ok.config(command=efectivizar)
        pay.bind("<Return>", lambda e: btn_ok.invoke() if btn_ok["state"] == "normal" else None)
        pay.bind("<Escape>", lambda e: pay.destroy())
        entry.focus_set()

        pay.update_idletasks()
        bw = pay.winfo_reqwidth()
        bh = pay.winfo_reqheight()
        bx = btn_cobrar.winfo_rootx()
        by = btn_cobrar.winfo_rooty()
        sx = pos.winfo_screenwidth()
        sy = pos.winfo_screenheight()
        x = min(bx, sx - bw - 4)
        y = max(0, by - bh - 8)
        pay.geometry(f"{bw}x{bh}+{x}+{y}")

    left = tk.Frame(pos, bg=COLOR_PANEL)
    left.grid(row=0, column=0, rowspan=2, sticky="nsw")
    for i in range(12):
        left.grid_rowconfigure(i, weight=0)
    left.grid_rowconfigure(99, weight=1)

    def boton_lateral(texto, color=None, fn=None):
        return tk.Button(
            left, text=texto, anchor="w",
            bg=color or COLOR_BTN, fg=COLOR_TEXT,
            activebackground="#505a62", activeforeground=COLOR_TEXT,
            relief="flat", padx=12, pady=10, font=("Segoe UI", 10, "bold"),
            width=16, command=fn
        )

    boton_lateral("Salir", COLOR_PRIMARY, fn=logout).grid(row=0, column=0, padx=8, pady=(8,4), sticky="ew")
    boton_lateral("Borrar todo", None, fn=limpiar_pedido).grid(row=1, column=0, padx=8, pady=4, sticky="ew")
    boton_lateral("Borrar ítem", None, fn=borrar_uno).grid(row=2, column=0, padx=8, pady=4, sticky="ew")

    header = tk.Frame(pos, bg=COLOR_BG)
    header.grid(row=0, column=1, sticky="ew", padx=8, pady=(8,4))
    header.grid_columnconfigure(0, weight=1)
    header.grid_columnconfigure(1, weight=1)
    header.grid_columnconfigure(2, weight=1)
    tk.Label(header, text=f"Usuario: {user_var.get() or '—'}",
             bg=COLOR_BG, fg=COLOR_TEXT, font=("Segoe UI", 12, "bold")).grid(row=0, column=1, sticky="n")

    center = tk.Frame(pos, bg=COLOR_PANEL)
    center.grid(row=1, column=1, sticky="nsew", padx=8, pady=4)
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(0, weight=1)
    center.grid_rowconfigure(1, minsize=100)

    ticket = tk.Text(center, bg=COLOR_TICKET_BG, fg=COLOR_TICKET_TXT,
                     font=("Consolas", 11), relief="flat", wrap="none", state="disabled", cursor="hand2")
    ticket.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

    def on_ticket_click(event):
        try:
            idx = ticket.index(f"@{event.x},{event.y}")
            line_no = int(idx.split(".")[0])
            seleccionar_por_linea(line_no)
        except:
            pass

    ticket.bind("<Button-1>", on_ticket_click)

    barra_total = tk.Label(center, text="  Ttl 0.00",
                           bg=COLOR_PRIMARY, fg="white",
                           font=("Segoe UI", 14, "bold"), padx=10, pady=8)
    barra_total.grid(row=1, column=0, sticky="ew", padx=8, pady=(0,8))

    right = tk.Frame(pos, bg=COLOR_PANEL)
    right.grid(row=0, column=2, rowspan=2, sticky="nse", padx=(4,8), pady=(8,4))
    right.grid_rowconfigure(0, weight=1)
    right.grid_columnconfigure(0, weight=0)
    right.grid_columnconfigure(1, weight=1)

    catlist = tk.Frame(right, bg=COLOR_PANEL)
    catlist.grid(row=0, column=0, sticky="ns", padx=(8,4), pady=4)

    options = tk.Frame(right, bg=COLOR_PANEL)
    options.grid(row=0, column=1, sticky="nsew", padx=(4,8), pady=4)

    COL_HEIGHT = 8
    COL_WIDTH  = 220

    def crear_opcion(texto, idx, bg=COLOR_PRIMARY):
        col = idx // COL_HEIGHT
        row = idx % COL_HEIGHT
        tk.Button(
            options, text=texto, width=18, height=2,
            bg=bg, fg="white", activebackground="#b11c25",
            relief="flat", font=("Segoe UI", 10, "bold"), padx=8, pady=8,
            command=lambda n=texto: on_product_click(n)
        ).grid(row=row, column=col, padx=8, pady=4, sticky="w")
        options.grid_columnconfigure(col, minsize=COL_WIDTH, weight=0)

    hamburguesas = ["Simple", "Doble", "Triple", "Promo2x1",
                    "Clasica simple", "Clasica doble", "Clasica triple",
                    "Clasica simple", "Clasica doble", "Clasica triple",
                    "Clasica simple", "Clasica doble", "Clasica triple"]

    def mostrar(cat):
        for w in options.winfo_children():
            w.destroy()
        if cat == "carne":
            for i, nombre in enumerate(hamburguesas):
                crear_opcion(nombre, i)
        else:
            crear_opcion("Dip Cheddar", 0, bg=COLOR_ORANGE)
            crear_opcion("Porción de Papas", 1)

    tk.Button(catlist, text="Hamburguesas",
              bg="#e5e7eb", fg="#111820", relief="flat",
              font=("Segoe UI", 10, "bold"), padx=10, pady=10,
              width=18, command=lambda: mostrar("carne")
    ).pack(fill="x", pady=(0,8))

    tk.Button(catlist, text="Extras",
              bg="#d6dbe1", fg="#111820", relief="flat",
              font=("Segoe UI", 10, "bold"), padx=10, pady=10,
              width=18, command=lambda: mostrar("extras")
    ).pack(fill="x")

    mostrar("carne")

    bottom = tk.Frame(pos, bg=COLOR_PANEL)
    bottom.grid(row=2, column=0, columnspan=3, sticky="ew", padx=8, pady=(4,8))
    bottom.grid_columnconfigure(0, weight=1)
    bottom.grid_columnconfigure(1, weight=0)

    clock_var = tk.StringVar()
    def tick():
        clock_var.set(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        bottom.after(1000, tick)

    tk.Label(bottom, textvariable=clock_var, bg=COLOR_PANEL, fg=COLOR_TEXT,
             font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", padx=10, pady=8)
    tick()

    btn_cobrar = tk.Button(bottom, text="Cobrar", command=cobrar,
                           bg=COLOR_GREEN, fg="white", relief="flat",
                           padx=16, pady=10, font=("Segoe UI", 10, "bold"))
    btn_cobrar.grid(row=0, column=1, padx=6, pady=6, sticky="e")

tk.Button(root, text="Ingresar", command=abrir_pos).pack(pady=10)
root.mainloop()
