os Python ka ek built-in module hai (matlab pehle se Python ke andar maujood hai, alag se install nahi karna padta) jo aapke operating system (Windows/Mac/Linux) se baat karne mein madad karta hai.
os Se Kya-Kya Kaam Le Sakte Hain (General):
Files/folders ko manage karna (banana, delete karna, dekh na)
Environment variables ko read karna (jo hum abhi use kar rahe hain)
System ki information nikalna (jaise current folder kaunsa hai)
os.getenv("DATABASE_URL") ka matlab hai: "System se puchho ke DATABASE_URL naam ka environment variable kya hai"
Jab humne .env file banayi thi aur load_dotenv() call kiya tha, to .env file ke andar likhi values (jaise DATABASE_URL=postgresql://...) temporarily environment variables ban jati hain. os.getenv() unhi ko wapas nikal kar deta hai.
BaseModel → Pydantic ka tool jo automatic data validation karta hai (jaise: agar email format galat hai, khud error de dega)
EmailStr → special type jo confirm karta hai diya gaya text valid email format mein hai (jaise something@something.com)
UserCreate class → signup ke waqt 3 cheezein expect karta hai: username, email, password
UserLogin class → login ke waqt sirf 2 cheezein: email, password
models.py = database table kaisi dikhti hai
schemas.py = API se data kaisa aana/jana chahiye