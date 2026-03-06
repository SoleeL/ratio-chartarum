from textual.app import App

from ratio_chartarum.adapters.ui.app import RatioChartarum
from ratio_chartarum.bootstrap.container import Container


def main() -> None:
    container = Container()
    ratio_chartarum: App = RatioChartarum(container)
    ratio_chartarum.run()


if __name__ == "__main__":
    main()
