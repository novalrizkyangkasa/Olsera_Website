import pytest
import time
from selenium import webdriver
from olsera_automation.list_modul.login import LoginPage
from olsera_automation.list_modul.selectstore import SelectStore
from olsera_automation.list_modul.addproduct import addproduct
import allure

@allure.feature("Base Page")
@pytest.fixture
def driver_setup():
    driver = webdriver.Chrome()
    
    # Melakukan login di sini agar bisa digunakan di semua test case
    login_page = LoginPage(driver)
    login_page.navigate_to("https://dashboard.olsera.co.id/login")
    login_page.enter_username("rizkynoval5@gmail.com")
    login_page.enter_password("noval123")
    login_page.click_login()

    yield driver  # Kembalikan driver untuk digunakan di test case lain

    driver.quit()  # Teardown WebDriver setelah semua test selesai

# Test case pertama: login dan verifikasi judul halaman
@allure.feature("Login Page")
def test_login(driver_setup):
    driver = driver_setup
    print("Title of the page after login is: ", driver.title)
    assert "Olsera" in driver.title


# Test case kedua: melanjutkan memilih toko dan input barang setelah login
@allure.feature("Add New Product")
def test_selectstore(driver_setup):
    driver = driver_setup
    select_store = SelectStore(driver)
    select_store.click_store()  # Mengklik toko dengan nama tertentu
    print("Successfully clicked store.")
    
    select_store.click_loginstore()

    user_name = select_store.assert_name()
    assert user_name.text == "Naufal Rizky_olseraqatest", "User Name tidak Sesuai!"

    select_store.dropdown_katalog()
    print("Successfully clicked katalog.")
    time.sleep(3)
    select_store.child_katalog()
    print("Successfully clicked katalog.")
    time.sleep(3)
    span_text = select_store.assert_page_produk()
    print("Successfully clicked produk.")
    assert span_text == "Products", "Page Products Tidak Sesuai!"
    time.sleep(3)
    select_store.add_product()
    print("Successfully access add new product.")
    time.sleep(3)
    span_text = select_store.assert_create_product_page()
    assert span_text == "Product Create", "Page Create Product Tidak Sesuai!"
    print("Successfully located on create product.")
    time.sleep(3)
    select_store.gambar_produk()
    print("Successfully upload image.")
    time.sleep(3)
    select_store.nama_produk()
    print("Successfully add product name.")
    time.sleep(3)
    select_store.nama_produk_alternatif()
    print("Successfully add alternative product name.")
    time.sleep(3)
    select_store.kategori_produk()
    print("Successfully add product category.")
    time.sleep(3)
    select_store.Harga_Jual_di_Toko()
    print("Successfully add price.")
    time.sleep(3)
    # select_store.toggle_harga_jual_online()
    # time.sleep(3)
    # select_store.toggle_lacak_inventori()
    # time.sleep(3)
    # select_store.inventori_jumlah_stock()
    # time.sleep(3)
    # select_store.inventori_peringatan_stock()
    # time.sleep(3)
    # select_store.inventori_fast_moving()
    # time.sleep(3)
    select_store.save_product()
    print("Successfully save a new product.")
    time.sleep(3)


# # Test case ketiga: melanjutkan memilih toko setelah login
# def test_addproduct(driver_setup):
#     driver = driver_setup
#     test_addproduct = addproduct(driver)
#     # test_addproduct.dropdown_katalog()
#     test_addproduct.child_katalog()
#     test_addproduct.assert_page_produk()
#     test_addproduct.add_product()
#     test_addproduct.assert_create_product_page()
#     test_addproduct.gambar_produk()
#     test_addproduct.nama_produk()
#     test_addproduct.nama_produk_alternatif()
#     test_addproduct.kategori_produk()
#     test_addproduct.Harga_Jual_di_Toko()
#     test_addproduct.toggle_harga_jual_online()
#     test_addproduct.toggle_lacak_inventori()
#     test_addproduct.inventori_jumlah_stock()
#     test_addproduct.inventori_peringatan_stock()
#     test_addproduct.inventori_fast_moving()
#     test_addproduct.save_product()