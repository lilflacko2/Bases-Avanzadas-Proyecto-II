from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
user = "neo4j"
password = "12345678"

driver = GraphDatabase.driver(uri, auth=(user, password))

def ejecutar_consulta():
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN n LIMIT 5")
        for record in result:
            print(record)

def close_connection():
    driver.close()

# Ejecutar consulta de ejemplo
ejecutar_consulta()
close_connection()
