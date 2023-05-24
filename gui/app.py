import customtkinter
from .buttons import MyCheckboxFrame, MyRadiobuttonFrame
from passgen.passgen import PassGen


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("400x260")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame_1 = MyCheckboxFrame(self, "Symbols", values=["a-z", "A-Z", "0-9", "#!$"])
        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.radiobutton_frame = MyRadiobuttonFrame(self, "Strength", values=["Simple", "Medium", "Strong", "Unbreakable"], app=self)
        self.radiobutton_frame.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

        self.textbox = customtkinter.CTkTextbox(master=self, height=5, corner_radius=0, activate_scrollbars=False)
        self.textbox.grid(row=3, column=0, padx=10, pady=5, sticky="nsew", columnspan=2)
        self.textbox.insert("0.0", "Your password will be here...")

        self.button = customtkinter.CTkButton(self, text="Save", command=self.save_password)
        self.button.grid(row=4, column=0, padx=10, pady=5, sticky="ew", columnspan=2)

        self.possible_to_save = False

    def insert_text(self, text):
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", text)

    def save_password(self):
        if self.possible_to_save:
            dialog = customtkinter.CTkInputDialog(text="Type in the password name", title="Save")

            with open("passwords.txt", "a", encoding="utf-8") as file:
                file.write(f"{dialog.get_input()}: {self.textbox.get('0.0', 'end')}")
        else:
            pass

    def generate_password(self):
        radio_info = self.radiobutton_frame.get()
        checkbox_info = self.checkbox_frame_1.get()
        
        if len(checkbox_info) == 0:
            self.possible_to_save = False
            self.insert_text("Choose at least one type of symbols above")
        else:
            self.possible_to_save = True
            passgen = PassGen({"strength": radio_info, 
                            "symbols": checkbox_info})
            password = passgen.generate_password()

            while passgen.generate_password is False:
                password = passgen.generate_password()

            self.insert_text(password)