from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import requests
driver = webdriver.Firefox()
TOKEN = input("Token: ")
ID = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": TOKEN}).json()['id']
script = """
function login(token) {
    setInterval(() => {
      document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
      location.reload();
    }, 2500);
  }

login('"""+TOKEN+"""');
"""
driver.get("https://dash.freeserver.tw/login")
login = driver.find_element(By.XPATH, "/html/body/div/main/section/div/div/div/div[1]/div/div[2]/button")
login.click()
driver.execute_script(script)
time.sleep(6)
auth = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div[2]/button[2]")
auth.click()
time.sleep(3)
try:
    password = driver.current_url.split("=")[1]
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/button[1]").click()
    time.sleep(3)
except:
    reset = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[4]/table/tbody/tr[2]/th/button")
    reset.click()
    time.sleep(3)
    password = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]").text.split(":")[1]
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/button[1]").click()
    time.sleep(3)
createb = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul/li[2]/a")
createb.click()
time.sleep(3)
name = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div/div/form/div[1]/input")
name.send_keys("wefhweufhwe")
time.sleep(3)
type = Select(driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div/div/form/div[2]/select"))
type.select_by_visible_text("程式語言 | Java")
time.sleep(3)
cpu = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div/div/form/div[4]/input")
cpu.send_keys("100")
time.sleep(3)
ram = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div/div/form/div[5]/input")
ram.send_keys("3215")
time.sleep(3)
disk = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div/div/form/div[6]/input")
disk.send_keys("10045")
time.sleep(3)
submit = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div/div/form/button")
submit.click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/button[1]").click() # ok button
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul/li[1]/a").click() # home page
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/table/tbody/tr/td[5]/a/button").click() # edit button
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div/div/button[2]").click() # go to panel
time.sleep(5)
json_data = {
    'user': ID,
    'password': password,
    'g-recaptcha-response': '03AFcWeA5stjnEfq3aZqsDM530TeGrtsvFyDmjEyYTKPzy_OyYHjiRN2fbiQ4ZtT2cvAjKnDCFefd6DZpr0EmJA8DN3jyiy0eV1btle_Ov0y-Ql_1b0Htr5KnyKF1iqXh9lgsNpTRb4kcFA38Ruc6BedsKFeqM0OWFYrFtCkfnPll-gX-b_dsMzpUqw2PDoW5FWfJVfbVDZ6vc46mHmQEpj_iW7Y54W1-ntrkHn6cmJiZTovu80fBOCyexGeGT2QhDDDDL5MKel51dXlqn4agp-wWOjbQ61TEIrz2DCC50DTVe4XQ6k23O7N7cxzVOPeWIaw4ABcRli6Hjxdndq8XDq8j8rKvymHZNVuDMdR8GR6wACA18W_XQEKCcPRRhc5dG83yrqJAz9e8PPHvx8u0URUmQeSVdzJC9yYpfNCEAZ9mZZ_7GPiKSUhQSR-osjl90QTSsS6ecV-L7DMkfrdP_PnGioOO1ABEjzlaEKUG-MW18RcpAiVnWA3_8tLdFPxRBEZj_zBJFDwEjBWQZm4KhRiZWWV5jPVfmtPb18wEjeFaWFclFUyGznNE11fqpY1keduDxBbPQ5Wwn4K3IXnyMxkkKVKEclpv7k6IFvEfjIVLP3RwLNFBc8f_m7g9auQiuIi5cwGs-rKok9ozouVpcGdPH62rWngttibC8UwW4nyQ0gy58Xy5di0jGr3PflWDDfRpEzYZLI9XUDQ8lwrPcoXUboOXP9M8w34H2n04lDEX9J9tP6BIAw8otTe99r32RTzsY3sFtR7no_PRMkuYJBdl1etDwSkUagCoD8y59E8NXhrBEjM-KHxmdtZryCoc1XDFtwT-8TVIJpobyaI2m6DCqdd7bBpelnYqnBHqt_jPT_JhTZLDsY8OJmz3xpRkwUDU4gpMKHMBtMm8exwJ362ihYyDc7HyrAY3N435Pzm9ic8v8vWwKsNsxzrC3lGTQOssvvdeM5d-BDZaqNrKeGNJBrWRK-VlM3HSZvgE3FF4n7fWnLt46UugLIDy7LYwvxqbkEXBduZQylVGt1rsiv69HJ6O733DsFQ_Y1ijCOuvStJCA3als93pgCyYi1kz0zwwOsHkS8S49a3p8OajHm-4DyXZOyweoapdQm5UcbV4XEYeEUlbo7tkObVjMtwfY-xBG4Y1xMY4wm06usmGxlarLNeEvROHtpGIxKi4ZxyddytXlqsvVjG2iZyThyRc_8ZMn2IToVX8Ytj8MZb4oMSDdxSjn8OMHjyvRRKWy4Mom6N7J-qSpVfDkfW-_oWvjmn_PacCtcBKBCszz8I5KdGCK1LE6j81Rfk9lTg5TkcTISrfwzl3T-lxjmmnpXH7mQiWjenrFWSWd0yRTHn0GjCcy-ZaMdZAoNYKNN1PVs3dlt8lU5Vc54dSVrr0XLy7ebGqKfFzvZLCwOrqjcz7rP7z8ugCZMdFkqbgIgcy1SYntJmp4sIZTott7FTiiXpwvJuQVTdP3mELO80uyXLWj8LDED1z2sW3nQgdeYBI4Pg-pc8igbv1JTygwhuzh6ftP_JHxBl3S6lovdpwBbpuriTjkK_fCs4jfO1ZzT3CBPO-Rs4ZNx4IZN0Z9y_rFaotrFemIjvZcSGQZ90uRJEi-9d_6-9jKMpkNx0jMM_HldvgYPgR7t-GySJk5XjJvw6MeprSXCyxmSGKtq9XOJLQSjeDIFKBBnU0USB1fUrT4i3wg_iGQUa5jMVQP5WEalqVOeLtuWymC8_9__ZFUQkznQ9VAr0ZXSsHsankMUu4S3LizbJLKHrnytC4',
}
response = requests.post('https://panel.freeserver.tw/auth/login',json=json_data)
time.sleep(3)
driver.refresh()
time.sleep(2000)
driver.close()