from jinja2 import Template
from datetime import datetime
import os


def generate_html_report(results, output_path="reports/test_report.html"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    template = """
    <html>
    <head><meta charset="UTF-8"><title>Socket Test Report</title></head>
    <body>
    <h1>Relatório de Testes de Integração</h1>
    <p>Executado em: {{ timestamp }}</p>
    <table border="1" cellpadding="5">
        <tr><th>Nome</th><th>Comando</th><th>Esperado</th><th>Resposta</th><th>Status</th></tr>
        {% for test in results %}
        <tr>
            <td>{{ test.name }}</td>
            <td>{{ test.command }}</td>
            <td>{{ test.expected }}</td>
            <td>{{ test.response }}</td>
            <td style="color: {% if test.status == '✅' %}green{% else %}red{% endif %};">{{ test.status }}</td>
        </tr>
        {% endfor %}
    </table>
    </body>
    </html>
    """
    report = Template(template).render(results=results, timestamp=now)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)