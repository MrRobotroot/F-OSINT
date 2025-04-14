import requests
import socket
import whois
import dns.resolver
from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

def banner():
    banner_text = """
   ____    ____  _________  ________  
  / __/   / __ \/ __/  _/ |/ /_  __/  
 / _/    / /_/ /\ \_/ //    / / /     
/_/      \____/___/___/_/|_/ /_/      
                                        
   🌐 Termux için OSINT Araç Takımı.
      MrRobotroot tarafından geliştirildi.
    """
    console.print(Panel.fit(banner_text, style="bold cyan"))

def username_search():
    sites = {
        "GitHub": "https://github.com/{}",
        "Twitter": "https://twitter.com/{}",
        "Instagram": "https://instagram.com/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "TikTok": "https://www.tiktok.com/@{}",
    }

    username = console.input("\n[bold cyan]> Aramak için kullanıcı adını girin: [/bold cyan]")
    console.print(f"\n[bold yellow]🔍 Aranıyor:[/bold yellow] [bold white]{username}[/bold white]\n")
    for site, url in sites.items():
        target = url.format(username)
        try:
            res = requests.get(target, timeout=5)
            if res.status_code == 200:
                console.print(f"[green][+] Site bulundu. {site}:[/green] {target}")
            elif res.status_code == 404:
                console.print(f"[red][-] Site bulunamadı. {site}[/red]")
            else:
                console.print(f"[yellow][!] {site} Kullanıcı bulamadık. {res.status_code}[/yellow]")
        except:
            console.print(f"[magenta][!] Bağlantı kurulurken hata oluştu {site}[/magenta]")
        sleep(0.5)

def ip_lookup():
    ip = console.input("\n[bold cyan]> Aramak için IP adresini girin: [/bold cyan]")
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        console.print(f"\n[bold green]🌍 IP Bilgisi:[/bold green]")
        for k, v in res.items():
            console.print(f"[cyan]{k}[/cyan]: [white]{v}[/white]")
    except:
        console.print("[red]❌ IP bilgisi alınamadı.[/red]")

def domain_lookup():
    domain = console.input("\n[bold cyan]> Domain gir (e.g. example.com): [/bold cyan]")
    try:
        w = whois.whois(domain)
        console.print(f"\n[bold green]🔎 WHOIS bilgisi:[/bold green]")
        for k, v in w.items():
            console.print(f"[cyan]{k}[/cyan]: [white]{v}[/white]")
    except:
        console.print("[red]❌ WHOIS denetleme başarısız.[/red]")

    try:
        console.print(f"\n[bold green]🧠 DNS Records:[/bold green]")
        for rtype in ["A", "MX", "NS"]:
            answers = dns.resolver.resolve(domain, rtype)
            for rdata in answers:
                console.print(f"[yellow]{rtype}[/yellow]: [white]{rdata.to_text()}[/white]")
    except:
        console.print("[red]❌ DNS denetleme başarısız.[/red]")

def main_menu():
    while True:
        banner()
        console.print("""
[bold blue]1.[/bold blue] Kullanıcı adı ile arama. 🔍
[bold blue]2.[/bold blue] IP Denetleyici. 🌍
[bold blue]3.[/bold blue] Domain Denetleyici. 🌐
[bold blue]4.[/bold blue] Çıkış. ❌
""")
        choice = console.input("[bold magenta]> Bir seçenek belirle: [/bold magenta]")

        if choice == "1":
            username_search()
        elif choice == "2":
            ip_lookup()
        elif choice == "3":
            domain_lookup()
        elif choice == "4":
            console.print("[bold red]Çıkılıyor...[/bold red]")
            break
        else:
            console.print("[red]Yanlış seçenek![/red]")  
console.print("\n[bold cyan]Menüye geri dönmek için enter basın...[/bold cyan]")  
input()  

if __name__ == "__main__":
    main_menu()
