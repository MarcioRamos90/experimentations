package database

import (
	"database/sql"

	"github.com/google/uuid"
)

type Course struct {
	db          *sql.DB
	ID          string
	Name        string
	Description string
	CategoryID  string
}

func NewCourse(db *sql.DB) *Course {
	return &Course{db: db}
}

func (c *Course) CreateCourse(name string, description string, category_id string) (Course, error) {

	_, err_query := c.db.Query("SELECT id FROM categories WHERE id = $1", category_id)

	if err_query != nil {
		return Course{}, nil
	}

	id := uuid.New().String()
	_, err := c.db.Exec("INSERT INTO courses(id, name, description, category_id) VALUES ($1, $2, $3, $4)", id, name, description, category_id)

	if err != nil {
		return Course{}, err
	}

	return Course{
		ID:          id,
		Name:        name,
		Description: description,
		CategoryID:  category_id,
	}, nil
}

func (c *Course) FindAll() ([]Course, error) {
	query, err := c.db.Query("SELECT * FROM courses")
	if err != nil {
		return nil, err
	}
	defer query.Close()
	courses := []Course{}

	for query.Next() {
		var id, name, description, category_id string
		if err := query.Scan(&id, &name, &description, &category_id); err != nil {
			return nil, err
		}
		courses = append(courses, Course{ID: id, Name: name, Description: description, CategoryID: category_id})
	}
	return courses, nil
}

func (c *Course) FindByCategoryID(category_id string) ([]Course, error) {
	query, err := c.db.Query("SELECT * FROM courses WHERE category_id = $1", category_id)
	if err != nil {
		return nil, err
	}
	defer query.Close()
	courses := []Course{}

	for query.Next() {
		var id, name, description, category_id string
		if err := query.Scan(&id, &name, &description, &category_id); err != nil {
			return nil, err
		}
		courses = append(courses, Course{ID: id, Name: name, Description: description, CategoryID: category_id})
	}
	return courses, nil

}
