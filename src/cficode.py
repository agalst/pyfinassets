from src.const import cfi_classes, cfi_types

class CFICode:
    code: str = ""

    def __init__(self, code:str):
        self.code = code
        self.first_char = self.code[0]
        self.second_char = self.code[1]
        self.third_char = self.code[2]
        self.fourth_char = self.code[3]
        self.fifth_char = self.code[4]
        self.sixth_char = self.code[5]

    def get_asset_class(self):
        return cfi_classes.get(self.first_char)

    def get_asset_type(self):
        return cfi_types.get(self.first_char + self.second_char)

    def get_asset_attribute1(self):
        pass

    def get_asset_attribute2(self):
        pass

    def get_asset_attribute3(self):
        pass

    def get_asset_attribute4(self):
        pass