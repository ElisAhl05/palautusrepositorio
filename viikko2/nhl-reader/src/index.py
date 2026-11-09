from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

def main():
    console = Console()
    
    while True:
        # Fråga efter säsong
        season = Prompt.ask(
            "Season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26]",
            default="2024-25"
        )
        if not season.strip():
            break

        # Fråga efter nationalitet
        nationality = Prompt.ask(
            "Nationality [USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS]",
            default="FIN"
        ).strip().upper()
        if not nationality:
            break

        # Bygg URL dynamiskt med vald säsong
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        
        try:
            reader = PlayerReader(url)
            stats = PlayerStats(reader)
            players = stats.top_scorers_by_nationality(nationality)
        except Exception as e:
            console.print(f"[red]Could not retrieve data: {e}[/red]")
            continue

        # Skapa en snygg tabell med Rich[cite: 37]
        table = Table(title=f"Season {season} players from {nationality}")
        
        table.add_column("Released", style="cyan", no_wrap=True)
        table.add_column("teams", style="magenta")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="bold green")

        # Lägg till spelarna i tabellen
        for player in players:
            # Beräkna totalpoäng (mål + assist)
            points = player.goals + player.assists
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(points)
            )

        # Skriv ut tabellen till terminalen
        console.print(table)
        console.print() # Tom rad för snyggare flöde

if __name__ == "__main__":
    main()