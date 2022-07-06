import React, { useCallback, useState } from 'react'

function App (props) {
  const [count, setCount] = useState(0)

  const increment = useCallback(() => {
    setCount(count => count + 1)
  }, [count])

  return (
    <main>
      <h1>{props.greeting}</h1>
      <h2>Build an amazing React SPA with Django!</h2>
      <button onClick={increment}>Clicked {count} times</button>
      <footer>
        <p>©{new Date().getFullYear()} Licensed under <a href="https://opensource.org/licenses/MIT" target="_blank">MIT license</a>.</p>
      </footer>
    </main>
  )
}

export default App
