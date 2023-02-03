import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_janga_prod():
    # options
    options = webdriver.ChromeOptions()

    # user-agent
    options.add_argument(
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

    # for ChromeDriver version
    options.add_argument("--disable-blink-features=AutomationControlled")

    # headless mode
    # options.add_argument("--headless")
    # options.headless = True

    driver = webdriver.Chrome(
        executable_path="/home/user/git/parser_jung_by/ChromeDrive/chromedriver",
        options=options
    )

    # url
    url = "https://rabota.by/employer/vacancyresponses?vacancyId=75922811"

    # name_product = "jung-ls-plus"
    # list item
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    r = requests.get(url=url, headers=headers)

    with open("html/rabota_by_4.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    # product_cards = soup.find_all("div", class_="resume-search-item__header")
    product_url_dict = soup.find_all("span", class_="bloko-header-section-3")
    product_dict={}

    # print(product_url_dict)
    username = "levkovichvadzim@gmail.com"
    passdw = "6zuzQGG2"
    for product in product_url_dict:
        product_url = product.find("a", class_="serp-item__title").get("href")
        print(product_url)
        driver.get(product_url)
        button_discription = driver.find_element(By.XPATH, "(//a[@class='supernova-button'])[1]")
        button_discription.click()
        button_pass_click = driver.find_element(By.XPATH, "(//button[contains(text(),'Войти с паролем')])[1]")
        button_pass_click.click()
        driver.find_element(By.XPATH, "(//input[@placeholder='Электронная почта или телефон'])[1]").send_keys(username)
        driver.find_element(By.XPATH, "(//input[@placeholder='Пароль'])[1]").send_keys(passdw)
        driver.find_element(By.XPATH, "(//button[@class='bloko-button bloko-button_kind-primary'])[1]").click()
        break

    for product in product_url_dict:
        product_url = product.find("a", class_="serp-item__title").get("href")
        print(product_url)
        driver.get(product_url)
        time.sleep(3)
        driver.find_element(By.XPATH, "((//div[@class='bloko-gap bloko-gap_bottom'])[1])").click()
        driver.find_element(By.XPATH, "(//span[contains(text(),'Подумать')])[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//button[@data-qa='negotiations-change-topic__submit'])[1]").click()
        time.sleep(3)
        driver.stop_client()
    driver.close()
    driver.quit()


    # for product in product_cards:
    #     product_url = product.find("a", class_="serp-item__title").get("href")
    #     k+=1
    #     print(product_url)
        # product_title = product.find("div", "product-title").text.strip()
        # product_article_id = product.find_all("td", "product-properties__value")[2].text.strip()
        # product_img = "https://jung-pro.ru/" + product.find("img").get("src")
        # product_other = product.find_all("td", class_="table-col introtext-col")
        # y = len(product_other)
        # for q in range(y):
        #     try:
        #         product_other[q] = product.find_all("td", class_="table-col introtext-col")[q].text.strip()
        #
        #         with open("html/page_source_7_jung-a-creation.html") as file:
        #             src = file.read()
        #         soup = BeautifulSoup(src, "lxml")
        #         product_brand = soup.find_all("td", class_="product-properties__value")[0].text.strip()
        #         product_series = soup.find_all("td", class_="product-properties__value")[1].text.strip()
        #         product_article = soup.find_all("td", class_="product-properties__value")[2].text.strip()
        #         product_material = soup.find_all("td", class_="product-properties__value")[3].text.strip()
        #         product_color = soup.find_all("td", class_="product-properties__value")[4].text.strip()
        #         product_type = soup.find_all("td", class_="product-properties__value")[5].text.strip()
        #         product_kind_material = soup.find_all("td", class_="product-properties__value")[6].text.strip()
        #         product_type_surface = soup.find_all("td", class_="product-properties__value")[7].text.strip()
        #         product_halogen_free = soup.find_all("td", class_="product-properties__value")[8].text.strip()
        #         product_mounting_orientation = soup.find_all("td", class_="product-properties__value")[9].text.strip()
        #         product_field_of_inscription = soup.find_all("td", class_="product-properties__value")[10].text.strip()
        #         product_height = soup.find_all("td", class_="product-properties__value")[11].text.strip()
        #         product_width = soup.find_all("td", class_="product-properties__value")[12].text.strip()
        #         product_without_baffle = soup.find_all("td", class_="product-properties__value")[13].text.strip()
        #         product_hinged_lid = soup.find_all("td", class_="product-properties__value")[14].text.strip()
        #         product_degree_of_protection = soup.find_all("td", class_="product-properties__value")[15].text.strip()
        #         product_number_of_posts = soup.find_all("td", class_="product-properties__value")[16].text.strip()
        #
        #         product_dict[product_article_id] = {
        #             "product_title": product_title,
        #             "product_brand": product_brand,
        #             "product_series": product_series,
        #             "product_article": product_article,
        #             "product_material": product_material,
        #             "product_color": product_color,
        #             "product_type": product_type,
        #             "product_kind_material": product_kind_material,
        #             "product_type_surface": product_type_surface,
        #             "product_halogen_free": product_halogen_free,
        #             "product_mounting_orientation": product_mounting_orientation,
        #             "product_field_of_inscription": product_field_of_inscription,
        #             "product_height": product_height,
        #             "product_width": product_width,
        #             "product_without_baffle": product_without_baffle,
        #             "product_hinged_lid": product_hinged_lid,
        #             "product_degree_of_protection": product_degree_of_protection,
        #             f"product_other_0": product_other[0],
        #             f"product_other_1": product_other[1],
        #             f"product_other_2": product_other[q],
        #             # "product_other_2": product_other_2,
        #             # "product_other_3": product_other_3,
        #             "product_number_of_posts": product_number_of_posts,
        #             "product_img": product_img
        #         }
        #
        #         with open("json/page_source_1_jung-a-creation.json", "w") as file:
        #             json.dump(product_dict, file, indent=4, ensure_ascii=False)
        #         break
        #
        #     except:
        #
        #         with open("html/page_source_1_jung-a-creation.html") as file:
        #             src = file.read()
        #         soup = BeautifulSoup(src, "lxml")
        #         product_brand = soup.find_all("td", class_="product-properties__value")[0].text.strip()
        #         product_series = soup.find_all("td", class_="product-properties__value")[1].text.strip()
        #         product_article = soup.find_all("td", class_="product-properties__value")[2].text.strip()
        #         product_material = soup.find_all("td", class_="product-properties__value")[3].text.strip()
        #         product_color = soup.find_all("td", class_="product-properties__value")[4].text.strip()
        #         product_type = soup.find_all("td", class_="product-properties__value")[5].text.strip()
        #         product_kind_material = soup.find_all("td", class_="product-properties__value")[6].text.strip()
        #         product_type_surface = soup.find_all("td", class_="product-properties__value")[7].text.strip()
        #         product_halogen_free = soup.find_all("td", class_="product-properties__value")[8].text.strip()
        #         product_mounting_orientation = soup.find_all("td", class_="product-properties__value")[9].text.strip()
        #         product_field_of_inscription = soup.find_all("td", class_="product-properties__value")[10].text.strip()
        #         product_height = soup.find_all("td", class_="product-properties__value")[11].text.strip()
        #         product_width = soup.find_all("td", class_="product-properties__value")[12].text.strip()
        #         product_without_baffle = soup.find_all("td", class_="product-properties__value")[13].text.strip()
        #         product_hinged_lid = soup.find_all("td", class_="product-properties__value")[14].text.strip()
        #         product_degree_of_protection = soup.find_all("td", class_="product-properties__value")[15].text.strip()
        #         product_number_of_posts = soup.find_all("td", class_="product-properties__value")[16].text.strip()
        #
        #         product_dict[product_article_id] = {
        #             "product_title": product_title,
        #             "product_brand": product_brand,
        #             "product_series": product_series,
        #             "product_article": product_article,
        #             "product_material": product_material,
        #             "product_color": product_color,
        #             "product_type": product_type,
        #             "product_kind_material": product_kind_material,
        #             "product_type_surface": product_type_surface,
        #             "product_halogen_free": product_halogen_free,
        #             "product_mounting_orientation": product_mounting_orientation,
        #             "product_field_of_inscription": product_field_of_inscription,
        #             "product_height": product_height,
        #             "product_width": product_width,
        #             "product_without_baffle": product_without_baffle,
        #             "product_hinged_lid": product_hinged_lid,
        #             "product_degree_of_protection": product_degree_of_protection,
        #             "product_number_of_posts": product_number_of_posts,
        #             "product_img": product_img
        #         }
        #
        #         with open("json/page_source_1_jung-a-creation.json", "w") as file:
        #             json.dump(product_dict, file, indent=4, ensure_ascii=False)
        #         break






def main():
    get_janga_prod()

if __name__ == '__main__':
    main()

