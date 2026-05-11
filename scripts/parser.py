from scapy.all import rdpcap
import pandas as pd
import sys

if len(sys.argv) < 3:
    print("Usage: python3 parser.py <pcap_file> <label>")
    sys.exit(1)

pcap_file = sys.argv[1]
label = sys.argv[2]

packets = rdpcap(pcap_file)
flows = {}

for pkt in packets:
    if pkt.haslayer("IP"):
        src = pkt["IP"].src
        dst = pkt["IP"].dst
        proto = pkt["IP"].proto
        key = (src, dst, proto)

        if key not in flows:
            flows[key] = {
                "packets": 0,
                "bytes": 0,
                "start_time": float(pkt.time),
                "end_time": float(pkt.time)
            }

        flows[key]["packets"] += 1
        flows[key]["bytes"] += len(pkt)
        flows[key]["end_time"] = float(pkt.time)

data = []

for (src, dst, proto), stats in flows.items():
    duration = stats["end_time"] - stats["start_time"]
    packets_per_sec = stats["packets"] / duration if duration > 0 else stats["packets"]

    data.append({
        "src_ip": src,
        "dst_ip": dst,
        "protocol": proto,
        "packets": stats["packets"],
        "bytes": stats["bytes"],
        "duration": duration,
        "packets_per_sec": packets_per_sec,
        "label": label
    })

df = pd.DataFrame(data)

output_file = f"dataset/csv/dataset_{label}.csv"
df.to_csv(output_file, index=False)

print(df)
print(f"\nSaved to {output_file}")
