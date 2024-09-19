from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from olsera_automation.default_page.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from faker import Faker
import os
import time

fake = Faker()

class addproduct(BasePage):
    def dropdown_katalog(self):
        """Click on Add Product button"""
        katalog_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/aside/section/div[2]/ul/li[1]/div/i'))
            )
        time.sleep(5)
        katalog_button.click()

    def child_katalog(self):
        self.driver.implicitly_wait(10)
        """Click on List of Product"""
        child_katalog_button = self.driver.find_element(By.XPATH, '//li[@role="menuitem"]/span[text()="Produk")]')
        child_katalog_button.click()
    
    def assert_page_produk(self):
         "assert page produk"
         produk_title = self.driver.find_element(By.XPATH, '//div[@class="breadcrumb-item"]/span[text()="Products")]')
         return produk_title
    
    def add_product(self):
        "add product"
        self.driver.implicitly_wait(10)
        product_button = self.driver.find_element(By.XPATH, '//button[contains(.,"Tambah")]')
        product_button.click()

    def assert_create_product_page(self):
        "assert create product page"
        create_product_title = self.driver.find_element(By.XPATH, '//span[@class="active"][text()="Product Create"]')
        return create_product_title
    
    def gambar_produk(self):
        self.driver.implicitly_wait(10)
        """Click on product image"""
        produk_upload = self.driver.find_element(By.XPATH, '//div[@class="el-upload el-upload--picture-card"]')
        produk_upload.click()
        image_path = os.path.abspath("/Users/noval/Documents/Learn Automation Testing/Olsera/olsera_automation/image.jpeg")
        produk_upload.send_keys(image_path)
    
    def nama_produk(self):
        self.driver.implicitly_wait(10)
        """Input product name"""
        product_name = self.driver.find_element(By.XPATH, '//input[@placeholder="Masukkan Nama Produk"]')
        product_name = fake.text(max_nb_chars=50)

    def nama_produk_alternatif(self):
        self.driver.implicitly_wait(10)
        """Input product alternative name"""
        product_alternative_name = self.driver.find_element(By.XPATH, '//input[@placeholder="Masukkan Nama Produk Alternatif"]')
        product_alternative_name = fake.text(max_nb_chars=50)

    def kategori_produk(self):
        self.driver.implicitly_wait(10)
        """Input product category"""
        product_category = self.driver.find_element(By.XPATH, '//div[@class="el-input el-input--medium el-input--suffix is-focus"]//input[@placeholder="Pilih salah satu"]')
        product_category.send_keys("Shockbreaker Mobil", Keys.ARROW_DOWN, Keys.ENTER)
    
    def Harga_Jual_di_Toko(self):
        self.driver.implicitly_wait(10)
        """Input product price"""
        product_price = self.driver.find_element(By.XPATH, '//div[@class="el-input el-input--medium"]//input[@class="el-input__inner" and @inputmode="decimal"]')
        product_price.send_keys("10000")
    
    def toggle_harga_jual_online(driver):
        toggle_harga_jual = driver.find_element(By.XPATH, "//div[@class='switch-varian flex-container el-col el-col-15']//strong")
       
        # Mendapatkan teks dari elemen tersebut (apakah 'Ya' atau 'Tidak')
        toggle_status = toggle_harga_jual.text
        if toggle_status == 'Ya':
            print("Value di field tersebut sudah 'Ya'")
        else:
            toggle_harga_jual.click()
    
    def toggle_lacak_inventori(driver):
        toggle_lacak_inventori = driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/section/div[2]/div/div[1]/div[2]/form/div[6]/div[2]/div/div/div/div[2]/strong")

        # Mendapatkan teks dari elemen tersebut (apakah 'Ya' atau 'Tidak')
        toggle_status = toggle_lacak_inventori.text
        if toggle_status == 'Ya':
            print("Value di field tersebut sudah 'Ya'")
        else:
            toggle_lacak_inventori.click()

    def inventori_jumlah_stock(self):
        self.driver.implicitly_wait(10)
        """Input product stock"""
        inventori_stock = self.driver.find_element(By.XPATH, '//label[normalize-space(text())="Jumlah stok yang tersedia saat ini"]/following::input[1]')
        inventori_stock.send_keys("10")
    
    def inventori_peringatan_stock(self):
        self.driver.implicitly_wait(10)
        """Input product warning stock"""
        inventori_warning_stock = self.driver.find_element(By.XPATH, '//label[normalize-space(text())="Peringatan Sisa Stok"]/following::input[1]')
        inventori_warning_stock.send_keys("2")
    
    def inventori_fast_moving(self):
        self.driver.implicitly_wait(10)
        """Input product fast moving"""
        inventori_fast_moving = self.driver.find_element(By.XPATH, '//label[normalize-space(text())="Qty Fast Moving"]/following::input[1]')
        inventori_fast_moving.send_keys("1")
    
    def save_product(self):
        self.driver.implicitly_wait(10)
        """Click on save button"""
        save_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        save_button.click()
