import time
import requests

def track_local_latency():
    url = "http://localhost:11434/"
    print("⏱️  Measuring loopback interface ping to offline engine...")
    
    start_time = time.time()
    try:
        response = requests.get(url, timeout=5)
        end_time = time.time()
        elapsed = (end_time - start_time) * 1000
        
        if response.status_code == 200:
            print(f"✅ Local Server Response Time: {elapsed:.2f} ms")
            print("🚀 Performance tier optimal for client-side processing.")
        else:
            print(f"⚠️ Server returned an anomaly code: {response.status_code}")
    except Exception:
        print("❌ Latency tracking failed. Background engine is completely unreachable.")

if __name__ == "__main__":
    track_local_latency()
