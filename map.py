from bs4 import BeautifulSoup
import re

def produce_post_info(fn):
    with open(fn, 'r') as fin:
        raw = fin.read()

    soup = BeautifulSoup(raw)
    items = soup.find_all('wp:author')
    # dc:creator field is identical to the author_login field.
    # pull out all author login fields
    results = []
    for item in items:
        id_num = list(item.find('wp:author_id').children)[0]
        login = list(item.find('wp:author_login').children)[0][7:-2]
        # display_name = item.find('wp:author_display_name').children[0][7:-2]
        first_name = list(item.find('wp:author_first_name').children)[0][7:-2]
        last_name = list(item.find('wp:author_last_name').children)[0][7:-2]
        slug = (first_name + '-' + last_name).lower()
        results.append((id_num, login, slug))
    return results


def main():
    posts_fn = 'wordpress-xml/scholarslab.wordpress.posts.xml'
    data = produce_post_info(posts_fn)

    users_fn = 'scholarslab.wordpress.people.xml'

    # slugs = produce_user_info(users_fn)
    print(data)

    # mappings = {}
    #
    # for author_id in users:
    #     mappings[users] = ''
    # # goal is to get a mapping of slugs to wordpress

if __name__ == '__main__':
    main()
