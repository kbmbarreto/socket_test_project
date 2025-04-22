import paramiko

def get_logs(host, username, password, log_path, lines=100):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)
        _, stdout, _ = ssh.exec_command(f'tail -{lines} {log_path}')
        logs = stdout.read().decode()
        ssh.close()
        return logs
    except Exception as e:
        return f"Erro ao buscar logs: {e}"