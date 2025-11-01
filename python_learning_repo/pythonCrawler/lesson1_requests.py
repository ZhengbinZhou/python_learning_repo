import requests

def get_html_text(url):
    try:
        headers = {
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        username = 'your_username'  # replace with your actual username
        password = 'your_password'  # replace with your actual password
        response = requests.get(url, headers=headers, timeout=100,auth=(username, password))
        response.raise_for_status()  # Raise an error for bad responses
        response.encoding = response.apparent_encoding
        return response.text

    except requests.exceptions.Timeout as e:
        return f"timeout: {e}"
    except requests.exceptions.HTTPError as e:
        return f"http error: {e}"
    except requests.exceptions.RequestException as e:
        return f"request exception: {e}"
    except Exception as e:
        return f"other error: {e}"


if __name__ == '__main__':#只有作为主程序运行时，才执行下面的代码，这一行是这个意思。
    url = "https://detail.tmall.com/item.htm?ali_refid=a3_420434_1006%3A1466230149%3AH%3AB2Nn7LSNGE1rAALIDzUKSw%3D%3D%3Ac7236201e189ed259cc60e9bf737da7d&ali_trackid=282_c7236201e189ed259cc60e9bf737da7d&id=758336684473&mi_id=0000AELIjHFckq6CfWWDoiyp3hwCIZuRMI7_jtUFwbthwpc&mm_sceneid=1_0_1820600181_0&priceTId=215044b717612087022503106e1173&skuId=5604445166562&spm=a21n57.1.hoverItem.4&utparam=%7B%22aplus_abtest%22%3A%22b2b9e0e9479154d1e6d2c38a14c319db%22%7D&xxc=ad_ztc"
    html_text = get_html_text(url)
    print(len(html_text))
