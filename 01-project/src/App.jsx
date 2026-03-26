import { useState } from "react"

const App = () => {

  const [news, setNews] = useState("")
  const [result, setResult] = useState("")
  const [loading, setLoading] = useState(false)

  const checkNews = async () => {

  if (!news.trim()) {
    setResult("⚠️ Please enter the news first")
    return
  }

  setLoading(true)

  const res = await fetch("http://127.0.0.1:5000/predict",{
    method:"POST",
    headers:{
      "Content-Type":"application/json"
    },
    body:JSON.stringify({
      text:news
    })
  })

  const data = await res.json()
  setResult(data.prediction)
  setLoading(false)
}
  
  return (
    <div className='min-h-screen bg-gradient-to-br from-black via-gray-900 to-gray-800 text-white flex items-center justify-center p-4'>
      
      <div className="w-full max-w-2xl bg-white/10 backdrop-blur-lg p-6 rounded-2xl shadow-2xl">

        <h1 className='text-3xl md:text-5xl font-bold text-center mb-6'>
          Fake News Detector 🧠
        </h1>

        <textarea 
        className='w-full p-3 rounded bg-black/50 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500'
        rows="4"
        placeholder='Enter news here...'
        value={news}
        onChange={(e) => setNews(e.target.value)}
        />

        <button 
          onClick={checkNews}
          className='mt-4 w-full bg-blue-600 hover:bg-blue-700 transition-all duration-300 py-2 rounded font-semibold active:scale-95'
        >
          {loading ? "Checking..." : "Check News"}
        </button>

        {result && (
          <div className="mt-6 text-center">
            <p className="text-xl">Result:</p>
            <p className={`text-2xl font-bold mt-2 ${
                result.includes("Fake") ? "text-red-400" :
                result.includes("Real") ? "text-green-400" :
                "text-yellow-400"
             }`}>
             {result}
            </p>
          </div>
        )}

      </div>
    </div>
  )
}

export default App