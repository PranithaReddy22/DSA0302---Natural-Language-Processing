import re

products = [
    "Apple iPhone 15",
    "Apple MacBook Air",
    "Samsung Galaxy S24",
    "Samsung Smart TV",
    "Dell Inspiron Laptop",
    "HP Pavilion Laptop",
    "Sony Headphones",
    "Boat Earbuds",
    "Canon Camera",
    "Nikon Camera",
    "Python Programming Book",
    "Java Programming Book"
]

print("=" * 60)
print("PRODUCT SEARCH SYSTEM")
print("=" * 60)

# Search Keywords
exact_keyword = "Sony Headphones"
prefix_keyword = "Apple"
suffix_keyword = "Camera"
partial_keyword = "Laptop"
case_keyword = "python"

def display_results(title, matches):
    print("\n" + title)
    print("-" * 40)
    if matches:
        for product in matches:
            print(product)
    else:
        print("No matching products found.")
    print("Total Matches:", len(matches))

exact_matches = [p for p in products if re.fullmatch(re.escape(exact_keyword), p)]

prefix_matches = [p for p in products if re.match(rf"{re.escape(prefix_keyword)}", p)]

suffix_matches = [p for p in products if re.search(rf"{re.escape(suffix_keyword)}$", p)]

partial_matches = [p for p in products if re.search(partial_keyword, p)]

case_matches = [p for p in products if re.search(case_keyword, p, re.IGNORECASE)]

display_results("1. Exact Keyword Search", exact_matches)
display_results("2. Prefix Search", prefix_matches)
display_results("3. Suffix Search", suffix_matches)
display_results("4. Partial Keyword Search", partial_matches)
display_results("5. Case-Insensitive Search", case_matches)


print("\n" + "=" * 60)
print("SEARCH REPORT")
print("=" * 60)
print("Exact Search Matches          :", len(exact_matches))
print("Prefix Search Matches         :", len(prefix_matches))
print("Suffix Search Matches         :", len(suffix_matches))
print("Partial Keyword Matches       :", len(partial_matches))
print("Case-Insensitive Matches      :", len(case_matches))
