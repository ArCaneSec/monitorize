import logging
import settings
from frames.app import app


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    settings.DEBUG_MODE and logger.info("App Started.")

    app.mainloop()
