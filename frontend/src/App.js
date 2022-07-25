import React from 'react';
import './App.css';

class App extends React.Component {
  constructor(props){
    super(props);
    this.state ={
      bookList:[],
      activeItem:{
        id:null, 
        name:'weird book',
        isbn:'1222838',
        author:''
      },
      authorList:[],
      authorItem:{
        id:null, 
        first_name:'',
        last_name:''
      },
      editing:false,
    }
    this.fetchBooks = this.fetchBooks.bind(this)
    this.fetchAuthors = this.fetchAuthors.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)

  };

  componentWillMount(){
    this.fetchBooks()
    this.fetchAuthors()
  }

  fetchAuthors(){
    console.log('fetching...')

    fetch('http://127.0.0.1:8000/api/authors/')
    .then(response => response.json())
    .then(data =>
      this.setState({
        authorList:data
      })
      )
  }

  fetchBooks(){
    console.log('fetching...')

    fetch('http://127.0.0.1:8000/api/books/')
    .then(response => response.json())
    .then(data =>
      this.setState({
        bookList:data
      })
      )
  }

  handleChange(e){
    var name = e.target.name
    var value = e.target.value
    console.log('Name', name)
    console.log('Value', value)

    this.setState({
      activeItem:{
        ...this.state.activeItem,
        name:value, 
      },
      authorItem:{
        ...this.state.authorItem,
        name:value, 
      }
    })
  }

  handleSubmit(e){
    e.preventDefault()
    console.log('ITEM:', this.state.activeItem)

    var url = 'http://127.0.0.1:8000/api/book/'
    fetch(url, {
      method:'POST',
      headers:{
        'Content-type':'application/json',
      },
      body:JSON.stringify(this.state.activeItem)
    }).then((response) => {
      this.fetchBooks()
      this.setState({
        activeItem:{
          id:null, 
          name:'',
          isbn:'',
          author:''
        }
      })
    }).catch(function(error){
      console.log('ERROR:', error)
    })
  }

  render(){

    var books = this.state.bookList
    var authors = this.state.authorList
    return(
      <div className='container'>

        <div id='task-container'>

          <div id='form-wrapper'>
          <form onSubmit={this.handleSubmit} id="form">
                      <div className="flex-wrapper">
                        <div style={{flex: 7}}>
                            <input onChange={this.handleChange} className="form-control" id="title"  type="text" name="name" placeholder="Book Name" />
                         </div>

                         
                      </div>
                      <div className="flex-wrapper">
                        <div style={{flex: 6}}>
                            <input  onChange={this.handleChange} className="form-control" id="title"  type="text" name="isbn" placeholder="ISBN" />
                         </div>
                         
                          <div style={{flex: 3}}>
                            <select name='Author' onChange={this.handleChange} className='form-control' placeholder="Author" id='author'>
                            <option selected disabled >--Select Author--</option>
                            {authors.map(function(author,index){
                              return(
                                <option key={index} value={author.author} >{author.first_name} {author.last_name}</option>
                              )
                            })}
                            </select>
                          </div>

                         <div style={{flex: 1}}>
                            <input id="submit" className="btn btn-warning" type="submit" name="Add" />
                          </div>
                      </div>
                </form>
          </div>

          <div id='list-wrapper'>
              {books.map(function(book, index){
                return(
                  <div key={index} className="book-wrapper flex-wrapper">
                    
                    <div style={{flex:5}}>
                    <span>{book.name}</span>
                    </div>
                    
                    <div style={{flex:2}}>
                    <span>{book.isbn}</span>
                    </div>
                    
                    <div style={{flex:2}}>
                    <span>{book.author.first_name} {book.author.last_name}</span>
                    </div>

                    <div style={{flex:1}}>
                        <button className='btn btn-sm btn-outline-info'>Edit</button>
                    </div>
                  </div>
                )
              })}
          </div>

        </div>

      </div>
    )
  }
}


export default App;
