import json
from socket_client import send_socket_command
from ssh_utils import get_logs
from utils.reporter import generate_html_report

# Configs
HOST = "127.0.0.1"
PORT = 8000
SSH_USER = "user"
SSH_PASS = "Teste@123"
LOG_PATH = "/home/server/googleProxy/socketProxy.log"

def run_all_tests():
    with open("test_cases.json", encoding="utf-8") as f:
        test_cases = json.load(f)

    results = []

    for test in test_cases:
        print(f"Executando: {test['name']}")
        response = send_socket_command(HOST, PORT, test['command'])
        expected = test["expected_start"]
        status = "✅" if expected in response else "❌"
        results.append({
            "name": test["name"],
            "command": test["command"],
            "expected": test["expected_start"],
            "response": response,
            "status": status
        })

    generate_html_report(results)
    print("\n✅ Relatório gerado em: reports/test_report.html")

    print("\n🧾 Últimos logs do servidor:")
    logs = get_logs(HOST, SSH_USER, SSH_PASS, LOG_PATH)
    print(logs)

if __name__ == "__main__":
    run_all_tests()