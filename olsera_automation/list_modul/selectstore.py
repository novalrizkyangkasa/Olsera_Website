from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from olsera_automation.default_page.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import requests
from faker import Faker

fake = Faker()

class SelectStore(BasePage):
    def click_store(self):
        """Select Active Store"""
        self.driver.implicitly_wait(10)
        try:
                store_field = self.driver.find_elements(By.XPATH, '//body/div[@id="app"]/div/div[1]/div[1]//*[contains(text(), "Hari")]')
                if store_field:
                     for store in store_field:
                          store.click()
                          break
                else:
                     print("Tidak ada toko aktif yang ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    def click_loginstore(self):
         "login to select store"
         self.driver.implicitly_wait(10)
         loginstore_button = self.driver.find_element(By.XPATH, '//span[contains(text(),"Masuk ke toko")]')
         loginstore_button.click()
    
    def assert_name(self):
         "assert user name"
         user_name = self.driver.find_element(By.XPATH, '//h5[contains(.,"Naufal Rizky_olseraqatest")]')
         return user_name
    
    def dropdown_katalog(self):
        """Click on Add Product button"""
        katalog_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/aside/section/div[2]/ul/li[1]/div/i'))
            )
        time.sleep(3)
        katalog_button.click()
    
    def child_katalog(self):
        self.driver.implicitly_wait(10)
        """Click on List of Product"""
        child_katalog_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/aside/section/div[2]/ul/li[1]/ul/a[1]/li/span'))
        )
        time.sleep(3)
        child_katalog_button.click()
    
    def assert_page_produk(self):
         "assert page produk"
         produk_title = self.driver.find_element(By.XPATH, '//span[@class="active"]')
         span_text = produk_title.text
         return span_text
    
    def add_product(self):
        "add product"
        self.driver.implicitly_wait(10)
        product_button = self.driver.find_element(By.XPATH, '//button[contains(.,"Tambah")]')
        product_button.click()

    def assert_create_product_page(self):
        "assert create product page"
        create_product_title = self.driver.find_element(By.XPATH, '//span[@class="active"][text()="Product Create"]')
        span_text = create_product_title.text
        return span_text
    
    def gambar_produk(self):
        """Click on product image"""
        produk_upload = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')) 
        )
        image_path = os.path.abspath("/Users/noval/Documents/Learn Automation Testing/Olsera/olsera_automation/image.jpeg")
        produk_upload.send_keys(image_path)

        # produk_upload = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div/div/ul/li/span'))
        # )

        url = 'https://api-dash.olsera.co.id/api/sukucadangmobil/admin/v1/id/product/upload'
        response = requests.get(url)
        if response.status_code == 201:
            api_data = response.json()
            api_url = api_data['url']

            if 'data' in api_data and 'status' in api_data and 'error' in api_data:
                if api_data['status'] == 201 and api_data['error'] == 0:
                    print("File uploaded successfully")

    
    def nama_produk(self):
        self.driver.implicitly_wait(10)
        """Input product name"""
        product_name = self.driver.find_element(By.XPATH, '//input[@placeholder="Masukkan Nama Produk"]')
        product_name_text = fake.text(max_nb_chars=50)
        product_name.send_keys(product_name_text)

        WebDriverWait(self.driver, 10).until(
            lambda driver:product_name.get_attribute('value') == product_name_text
        )

    def nama_produk_alternatif(self):
        self.driver.implicitly_wait(10)
        """Input product alternative name"""
        product_alternative_name = self.driver.find_element(By.XPATH, '//input[@placeholder="Masukkan Nama Produk Alternatif"]')
        product_alternative_name_text = fake.text(max_nb_chars=50)
        product_alternative_name.send_keys(product_alternative_name_text)

        WebDriverWait(self.driver, 10).until(
            lambda driver:product_alternative_name.get_attribute('value') == product_alternative_name_text
        )

    def kategori_produk(self):
        self.driver.implicitly_wait(10)
        """Input product category"""
        product_category = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div[2]/div/div[1]/div[2]/form/div[4]/div[2]/div/div/div/div[1]/input'))
        )
        product_category.send_keys("Shockbreaker Mobil")
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//li[contains(.,"Shockbreaker Mobil")]'))
        )
        action = ActionChains(self.driver)
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    
    def Harga_Jual_di_Toko(self):
        self.driver.implicitly_wait(10)
        """Input product price"""
        product_price = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="el-input el-input--medium"]//input[@class="el-input__inner" and @inputmode="decimal"]'))
        )
        product_price.send_keys("1000000")

        WebDriverWait(self.driver, 10).until(
            lambda driver:product_price.get_attribute('value') == "Rp 1.000.000"
        )
    
    # def toggle_harga_jual_online(driver):
    #     toggle_harga_jual = WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div[2]/div/div[1]/div[2]/form/div[5]/div[2]/div[2]'))
    #     )
       
    #     # Mendapatkan teks dari elemen tersebut (apakah 'Ya' atau 'Tidak')
    #     toggle_status = toggle_harga_jual.text.strip()
    #     if toggle_status == 'Ya':
    #         print("Value di field tersebut sudah 'Ya'")
    #     else:
    #         toggle_press = WebDriverWait(driver, 10).until(
    #             EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div[2]/div/div[1]/div[2]/form/div[5]/div[2]/div[2]/div[1]/div/span'))
    #         )
    #         toggle_press.click()
    
    # def toggle_lacak_inventori(driver):
    #     toggle_lacak_inventori = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/section/div[2]/div/div[1]/div[2]/form/div[6]/div[2]/div/div/div/div[2]/strong")

    #     # Mendapatkan teks dari elemen tersebut (apakah 'Ya' atau 'Tidak')
    #     toggle_status = toggle_lacak_inventori.text
    #     if toggle_status == 'Ya':
    #         print("Value di field tersebut sudah 'Ya'")
    #     else:
    #         toggle_lacak_inventori.click()

    # def inventori_jumlah_stock(self):
    #     self.driver.implicitly_wait(10)
    #     """Input product stock"""
    #     inventori_stock = self.driver.find_element(By.XPATH, '//label[normalize-space(text())="Jumlah stok yang tersedia saat ini"]/following::input[1]')
    #     inventori_stock.send_keys("10")
    
    # def inventori_peringatan_stock(self):
    #     self.driver.implicitly_wait(10)
    #     """Input product warning stock"""
    #     inventori_warning_stock = self.driver.find_element(By.XPATH, '//label[normalize-space(text())="Peringatan Sisa Stok"]/following::input[1]')
    #     inventori_warning_stock.send_keys("2")
    
    # def inventori_fast_moving(self):
    #     self.driver.implicitly_wait(10)
    #     """Input product fast moving"""
    #     inventori_fast_moving = self.driver.find_element(By.XPATH, '//label[normalize-space(text())="Qty Fast Moving"]/following::input[1]')
    #     inventori_fast_moving.send_keys("1")
    
    def save_product(self):
        self.driver.implicitly_wait(10)
        """Click on save button"""
        save_button = self.driver.find_element(By.XPATH, '//button[contains(.,"Simpan")]')
        save_button.click()

        url = 'https://api-dash.olsera.co.id/api/sukucadangmobil/admin/v1/id/product'
        response = requests.post(url)
        if response.status_code == 201:
            api_data = response.json()
            api_url = api_data['url']

            if 'data' in api_data and 'status' in api_data and 'error' in api_data:
                if api_data['status'] == 201 and api_data['error'] == 0:
                    print("Data Create successfully")

   