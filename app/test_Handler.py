import tornado.web

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('../test.html',)
        """
        coll = self.application.db.blog
        blog = coll.find_one()
        if blog:
            self.render('blog.html',
            page_title = blog["title"],
            blog = blog,
            )
        else:
            self.redirect("/")
        """
