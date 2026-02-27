from textual.app import App

from ratio_chartarum.adapters.ui.app import RatioChartarum


def main() -> None:
    ratio_chartarum: App = RatioChartarum()
    ratio_chartarum.run()


if __name__ == "__main__":
    main()
