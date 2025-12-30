# run in cmd(as admin) pip install speedtest-cli

import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()

    print("Testing speed...")

    st.get_best_server()

    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000
    ping = st.results.ping

    return {
        "download": round(download, 2),
        "upload": round(upload, 2),
        "ping": round(ping, 2)
    }

speed = check_internet_speed()

print(f"Download: {speed['download']} Mbps")
print(f"Upload: {speed['upload']} Mbps")
print(f"Ping: {speed['ping']} ms")

