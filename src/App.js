import './App.css';
import {useState, useEffect} from 'react'
import axios from 'axios'
import Add from './components/Add'
import Edit from './components/Edit'
import Footer from './components/Footer'

const App = () => {
  const [albums, setAlbums] = useState([])

  const getAlbums = () => {
    axios.get('https://young-savannah-30515.herokuapp.com/api/albums')
         .then(
           (response) => setAlbums(response.data),
           // console.log(response.data)
           (err) => console.err(err)
    )
    .catch((error) => console.error(error))
  }

  const handleCreate = (newAlbum) => {
    axios.post('https://young-savannah-30515.herokuapp.com/api/albums', newAlbum)
         .then(
           setAlbums([...albums, newAlbum])
         )
  }

  const handleDelete = (deletedAlbum) => {
    axios.delete('https://young-savannah-30515.herokuapp.com/api/albums/' + deletedAlbum.id)
         .then((response) => {
           setAlbums(
             albums.filter((album) => album.id !== deletedAlbum.id )
           )
         })
  }

  const handleUpdate = (album2Update) => {
    axios.put('https://young-savannah-30515.herokuapp.com/api/albums/' + album2Update.id, album2Update)
         .then( (response) => {
           setAlbums(
             albums.map((album) => {
               return album.id !== album2Update.id ? album : album2Update
             })
           )
         })
  }


  useEffect(() => {
    getAlbums()
  }, [])

  return (
    <body>
      <h1>Music Collection App</h1>
      <h2>Artists and Albums</h2>
      <Add handleCreate={handleCreate} />
      <div className="album-container">
        {albums.map((album)=> {
          return(
            <div key={album.id} className="card">
              <h3>{album.name}, {album.year}</h3>
              <Edit handleUpdate={handleUpdate} album={album} />
              <button onClick={() => {handleDelete(album)}}>Delete album</button>
            </div>
          )
        })}
      </div>
      <Footer />
    </body>
  )
}

export default App;
