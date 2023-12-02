import shlex, subprocess
import traceback
from aiogram.utils.markdown import quote_html


def run_command(command: str) -> str:
    cmd = shlex.split(command)
    try:
        process = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        stdout, stderr = process.stdout, process.stderr
    except subprocess.TimeoutExpired:
        stdout, stderr = '', traceback.format_exc()
    except FileNotFoundError:
        stdout, stderr = '', 'Комманда не найдена'
    txt = f'''<b>⚙️Комманда:</b> <code>{command}</code>

<b>💎Результат</b>:\n<code>{quote_html(stdout)}</code>

<b>🚫Ошибки</b>:\n<code>{quote_html(stderr)}</code>'''
    return txt

