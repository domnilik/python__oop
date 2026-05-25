from app import BankApplication
from cli import BankCLI

def main() -> None:
    """Точка входа в консольное приложение."""
    storage_file = "accounts_db.json"
    app_core = BankApplication(storage_path=storage_file)
    ui = BankCLI(app=app_core)
    ui.run()

if __name__ == "__main__":
    main()