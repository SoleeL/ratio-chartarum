from textual.app import App

from ratio_chartarum.adapters.ui.app import RatioChartarum


def main() -> None:
    ratioChartarum: App = RatioChartarum()
    ratioChartarum.run()


if __name__ == "__main__":
    main()
