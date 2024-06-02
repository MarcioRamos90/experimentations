package main

import (
	"io"
	"net/http"
	"os"

	"github.com/go-chi/chi"
	"github.com/go-chi/chi/middleware"

	"text/template"
)

type Templates struct {
	templates *template.Template
}

func (t *Templates) Render(w io.Writer, name string, data interface{}, c chi.Context) error {
	return t.templates.ExecuteTemplate(w, name, data)
}

func NewTemplates() *Templates {
	return &Templates{
		templates: template.Must(template.ParseGlob("views/*.html")),
	}
}

type Inventory struct {
	Material string
	Count    uint
}

func main() {
	r := chi.NewRouter()

	r.Use(middleware.Logger)
	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		sweaters := Inventory{"wool", 17}
		tmpl, err := template.New("test").Parse("{{.Count}} items are made of {{.Material}}")
		if err != nil {
			panic(err)
		}
		err = tmpl.Execute(os.Stdout, sweaters)
		w.Write(tmpl.)
	})

	http.ListenAndServe(":3000", r)
}
