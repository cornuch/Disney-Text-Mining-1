import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
        ],
        nav=True,
        label="Applications",
    ),
    brand="Web Scraping Booking",
    color="secondary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [
        navbar,
        dash.page_container
    ],
    fluid=False,
)


if __name__ == "__main__":
    app.run(debug=True)