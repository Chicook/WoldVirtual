from Metaverso_Crypto.webadministrativa.Blockchain_Principal.Publico.servidor.avatarbs2 import log_action

def procesar_transaccion(transaccion):
    log_action(f"Procesada transacción: {transaccion}")

def validar_transaccion(transaccion):
    es_valida = True  # Supongamos que la validación es exitosa
    log_action(f"Transacción validada: {transaccion} - Válida: {es_valida}")
    return es_valida
