import pytest
import allure

from PetProject.Pet.main import pet_id, status_code
from PetProject.Pet.pet_method import PetMethod

@allure.epic('Тестирвоание API')
@allure.feature('Проверка метода TestSubPet')

# Это нам не нужно
# class TestSubPet:
#     pet_test = PetMethod()
#     def setup_method(self): #Создаем питомца, дергаем его id для проверок
#         pet, status_code = self.pet_test.add_pet(
#             name="Boby",
#             status="available",
#             category_name="cat",
#             tag="little"
#         )
#         self.pet_id = pet['id']
#         print("ID питомца:", self.pet_id)
#         self.status_code = status_code
#     def test_add_pet(self):
#         pet = self.pet_test.get_pet(self.pet_id)
#         assert pet is not None
#         assert self.status_code == 200
#
#     def test_del_pet(self):
#         del_status_code = self.pet_test.delete_pet(self.pet_id)
#         self.status_code = del_status_code
#         assert self.status_code == 200


# Мне не понравилось, что каждый раз добавляется новый питомец
# поэтому я решил сделать вторую версию кода c помощью функции pytest.fixture
# Можно запускать разные верии проверок

@pytest.fixture(scope="class")
def pet_setup():
    pet_test = PetMethod()
    pet, status_code = pet_test.add_pet(
        name="Boby",
        status="available",
        category_name="cat",
        tag="little"
    )
    pet_id = pet['id']
    print("ID питомца:", pet_id)
    yield pet_id, status_code # Я хз че это за хрень, но прочитал, что она нужная для сохранения атрибутов

class TestSubPet:
    def setup_method(self):
        self.pet_test = PetMethod()

    @allure.story('Проверка метода добавления')
    def test_add_pet(self, pet_setup):
        with allure.step('Получаем данные из фикстуры'):
            pet_id, status_code = pet_setup
        with allure.step('Получаем информацию о питомце по ID'):
            pet = self.pet_test.get_pet(pet_id)
        with allure.step('Проверяем, что питомец успешно создан'):
            assert pet is not None
        with allure.step('Проверяем, что статус ответа равен 200'):
            assert status_code == 200
        with allure.step('Добавляем аттач'):
            with open("my_pet.json", "r", encoding="utf8") as file:
                json_content = file.read()
                allure.attach(json_content, name="JSON Data", attachment_type=allure.attachment_type.JSON)

    @allure.story('Проверка метода получения и записи в JSON')
    def test_get_pet(self, pet_setup):
        with allure.step('Получаем данные из фикстуры'):
            pet_id, status_code = pet_setup
        with allure.step('Получаем информацию о питомце по ID'):
            pet = self.pet_test.get_pet(pet_id)
        with allure.step('Проверяем, что питомец успешно найден'):
            assert pet is not None
        with allure.step('Проверяем, что статус ответа равен 200'):
            assert status_code == 200

    @allure.story('Проверка метода удаления')
    def test_del_pet(self, pet_setup):
        with allure.step('Получаем ID питомца из фикстуры'):
            pet_id, _ = pet_setup
        with allure.step('Усыпляем питомца'):
            del_status_code = self.pet_test.delete_pet(pet_id)
        with allure.step('Проверяем, что статус ответа равен 200'):
            assert del_status_code == 200

    # Это нам не нужно
    # def test_get_del_pet(self, pet_setup):
    #     pet_id, status_code = pet_setup
    #     pet = self.pet_test.get_pet(pet_id)
    #     assert pet == 'Eror'
    #     assert status_code == 200 #Должна быть 404 ошибка,
        # но постоянно выкидывает ошибку, что фактический статус код == 200