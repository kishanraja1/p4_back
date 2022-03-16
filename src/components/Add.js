import {useState} from 'react'

const Add = (props) => {
  let emptyAlbum = {name: '', year: 0}
  const [album, setAlbum] = useState(emptyAlbum)

  const handleChange = (e) => {
    setAlbum({...album, [e.target.name]: e.target.value})
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    props.handleCreate(album)
  }

  return (
    <div className="add-new-album">
      <details>
        <summary>Add New Album</summary>
        <form onSubmit={handleSubmit}>
          <label htmlFor="name">Album name: </label>
          <input type="text" name="name" placeholder="Thriller" onChange={handleChange}/><br/>
          <label htmlFor="year">Released: </label>
          <input type="number" name="year" placeholder="1982" onChange={handleChange}/><br/>
          <input type="submit" /> 
        </form>
      </details>
    </div>
  )
}

export default Add
