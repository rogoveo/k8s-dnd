import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


HOST = "0.0.0.0"
PORT = 8080
DATA_DIR = Path("/data")
NOTES_FILE = DATA_DIR / "party.log"


def read_notes() -> str:
    if not NOTES_FILE.exists():
        return "Журнал партии пока пуст."
    return NOTES_FILE.read_text(encoding="utf-8").strip() or "Журнал партии пока пуст."


def append_note(note: str) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with NOTES_FILE.open("a", encoding="utf-8") as handle:
        handle.write(note.strip() + "\n")


def render_index() -> str:
    kingdom = os.getenv("KINGDOM_NAME", "Неизвестное королевство")
    quest = os.getenv("QUEST_NAME", "Квест еще не назначен")
    token = os.getenv("DRAGON_TOKEN", "")
    token_state = "получен" if token else "не найден"
    notes = read_notes().replace("\n", "<br>")
    return f"""<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <title>Quest Board</title>
    <style>
      body {{
        font-family: Georgia, serif;
        max-width: 860px;
        margin: 40px auto;
        padding: 0 16px;
        background: #f3efe2;
        color: #2c2418;
      }}
      .card {{
        background: #fffaf0;
        border: 2px solid #6e4f2a;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
      }}
      code {{
        background: #efe4c8;
        padding: 2px 6px;
        border-radius: 6px;
      }}
    </style>
  </head>
  <body>
    <div class="card">
      <h1>Доска квестов таверны</h1>
      <p><strong>Королевство:</strong> {kingdom}</p>
      <p><strong>Текущий квест:</strong> {quest}</p>
      <p><strong>Секретный токен:</strong> {token_state}</p>
      <p><strong>Каталог заметок:</strong> <code>{DATA_DIR}</code></p>
      <h2>Журнал партии</h2>
      <p>{notes}</p>
      <h2>Подсказка</h2>
      <p>Добавьте запись запросом <code>POST /note?text=dragon+defeated</code>.</p>
    </div>
  </body>
</html>"""


class QuestBoardHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"ok")
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(render_index().encode("utf-8"))

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path != "/note":
            self.send_response(404)
            self.end_headers()
            return

        note = parse_qs(parsed.query).get("text", [""])[0]
        if note:
            append_note(note)

        self.send_response(201)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("note saved".encode("utf-8"))

    def log_message(self, format: str, *args) -> None:
        return


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), QuestBoardHandler)
    server.serve_forever()
