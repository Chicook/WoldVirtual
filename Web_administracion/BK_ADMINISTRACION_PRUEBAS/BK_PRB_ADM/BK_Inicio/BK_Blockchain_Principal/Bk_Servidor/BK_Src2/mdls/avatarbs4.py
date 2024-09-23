from Wold_Virtual.BK_Adm_prb.BK_Inicio.BK_Blockchain_Principal.Bk_Servidor.BK_Src2.dtbs.avatarbs2 import log_action

def procesar_transaccion(transaccion):
    log_action(f"Procesada transacción: {transaccion}")

def validar_transaccion(transaccion):
    es_valida = True  # Supongamos que la validación es exitosa
    log_action(f"Transacción validada: {transaccion} - Válida: {es_valida}")
    return es_valida
