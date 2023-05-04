import tkinter as tk
import requests
import time


class WeatherApp(tk.Tk):
    """Weather application class"""

    API_KEY = "27250b43ee3dba5b4cada9211e9b0758"
    LOCATION = "Rio de Janeiro,BR"

    def __init__(self):
        super().__init__()
        self.title('Tempo e clima')
        self.geometry('445x590')
        self.resizable(0, 0)
        self.weather_label = tk.Label(
            self, text="Previsão do tempo", fg="blue", font=('Helvetica', 24)
        )
        self.weather_label.pack(pady=10)
        self.temp_label = tk.Label(
            self, text="", fg="blue", font=('Helvetica', 48)
        )
        self.temp_label.pack()
        self.desc_label = tk.Label(
            self, text="", fg="blue", font=('Helvetica', 18)
        )
        self.desc_label.pack(pady=10)
        self.clock_label = tk.Label(
            self, text="Relógio", font=('Helvetica', 48)
        )
        self.clock_label.pack(pady=20)
        self.money_label = tk.Label(
            self, text="Cotação", fg="blue", font=('Helvetica', 48)
        )
        self.money_label.pack(pady=20)
        self.after(0, self.update_weather)
        self.after(0, self.update_clock)
        self.after(0, self.update_money)

    def update_weather(self):
        """Update the weather information"""

        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={self.LOCATION}&units=metric&appid={self.API_KEY}"
            response = requests.get(url)
            data = response.json()
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].capitalize()
            self.temp_label.configure(text=f"{temp:.0f}°C")
            self.desc_label.configure(text=desc)
        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"Erro ao obter a previsão do tempo: {e}")
        self.after(600000, self.update_weather)

    def update_clock(self):
        """Update the clock"""

        now = time.strftime("%H:%M:%S")
        self.clock_label.configure(fg="blue", text=now)
        self.after(1000, self.update_clock)

    def update_money(self):
        """Update the currency exchange rates"""

        try:
            url = "https://api.exchangerate-api.com/v4/latest/BRL"
            response = requests.get(url)
            data = response.json()
            brl_rate = data["rates"]["BRL"]
            usd_rate = data["rates"]["USD"]
            eur_rate = data["rates"]["EUR"]
            self.money_label.configure(
                text=f"USD/BRL: {usd_rate:.2f}\n"
                     f"BRL/USD: {usd_rate:.2f}\n"
                     f"EUR/BRL: {eur_rate:.2f}\n"
            )
        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"Erro ao obter a cotação: {e}")
        self.after(1000, self.update_money)




if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
