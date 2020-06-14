# reverse_tcp_shell
Spawn a reverse tcp shell

On attacker's machine:

python reverse_shell_attacker.py

Attacker keeps listening for a connection, once target executes reverse_shell_target.py, a shell from target's machine is opened to attacker. So, attacker can execute system commands as he wants, without any authentication.

On Target's machine:

python reverse_shell_target.py (put attacker's ip address in script)

NO CREDENTIALS REQUIRED :)

Please use this tool for EDUCATIONAL PURPOSE ONLY.
