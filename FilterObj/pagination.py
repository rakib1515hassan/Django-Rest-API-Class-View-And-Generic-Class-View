from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


# NOTE Custom Pagination
class CustomPagination(PageNumberPagination):  # আলাদা আলাদা CustomPagination Class তৈরি করা যায় আলাদা আলাদা View.py class এর জন্যে।
    page_size = 3            # একটি Page এ কতগুলো Data দেখাবে তা বেলে দিব।
    # page_query_param = 'p' # এখানে যা লিখবো Url ও তাই লিখতে হবে, /?p=2
    page_size_query_param = 'page_size' # User থেকে input নিব সে কতগুলো Data 1 page এ দেখতে চায়।
    max_page_size = 6        # সর্বচ্চ কতগুলো Data দেখাবে, তার বেশি দেখাবে না। user 6 এর বেশি input দিলেও সর্বচ্চ 6 টি দেখাবে।  


class CustomPagination_1(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5








class CustomPagination_LO(LimitOffsetPagination):

    default_limit = 2                  # তাহেলে এখন প্রতি page এ 2 টি করে Data show করবে।
    # limit_query_param = 'my_limit'   # By defalult 'limit' যদি তা Change করতে চাই তবে এর মাধ্যমে তা করতে পারি।
    # offset_query_param = 'my_offset' # By defalult 'limit' যদি তা Change করতে চাই তবে এর মাধ্যমে তা করতে পারি।
    max_limit = 5                      # সর্বচ্চ কতগুলো Data দেখাবে, তার বেশি দেখাবে না। user limit = 6 বা তার বেশি দিলেও সর্বচ্চ 5 টি দেখাবে। 
    offset_query_description = 'offset=5' # কত থেকে Data দেখানো শুরু করবে তা এখানে বলে দিতে পারি।







## এই Pagination এ Previour and Next Button ছাড়া আর কিছু থাকে না। এটি আমাদের Model এ Created নামে একটি Field 
## কে Demand করে যার মাধ্যমে Data কে Ordering করে auto. যদি আমরা তা Model এর মধ্যে না দেই তবে Error দেখাবে।
## সে ক্ষেত্রে আমাদের কোন Field এর সাপেক্ষে Ordering করবে তা Menually বলে দিতে হবে।
class CustomPagination_CP(CursorPagination):
    page_size = 3
    ordering = 'name'
    # cursor_query_param = 'cursor' ## By default 'cursor' থাকে।
    # cursor_query_description = ''