import psycopg2
from datetime import datetime

def inserir_metrica_bd (completeness,
    validity,
    consistency,
    uniqueness,
    accuracy,
    timeliness,
    integrity,
    total):

    conn = psycopg2.connect(
        host="localhost",
        database="metrics",
        user="grafana",
        password="grafana"
    )

    cursor = conn.cursor()

    insert_sql = """
    INSERT INTO data_quality_metrics (
        data_execucao,
        completeness,
        validity,
        consistency,
        uniqueness,
        accuracy,
        timeliness,
        integrity,
        total_registros
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(insert_sql, (
        datetime.now(),
        completeness,
        validity,
        consistency,
        uniqueness,
        accuracy,
        timeliness,
        integrity,
        total
    ))

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    # Valores de exemplo para validar o fluxo de escrita no PostgreSQL.
    inserir_metrica_bd(
        completeness=98.50,
        validity=97.20,
        consistency=96.80,
        uniqueness=99.10,
        accuracy=95.75,
        timeliness=94.30,
        integrity=97.90,
        total=1000,
    )
    print("Metricas inseridas com sucesso em public.data_quality_metrics")