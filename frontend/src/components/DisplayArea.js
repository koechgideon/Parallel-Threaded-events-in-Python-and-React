import React, {useState, useEffect} from 'react'

const AppPage = () => {
   const [posts, setPosts] = useState([]);
   const WAIT_TIME = 500;
   useEffect(() => {
      const id = setInterval(() => {

                  fetch('http://127.0.0.1:8000/display/')
                     .then((response) => response.json())
                     .then((data) => {
                        console.log(data);
                        setPosts(data);
                     })
                     .catch((err) => {
                        console.log(err.message);
                     }); }, WAIT_TIME); return () => clearInterval(id);
               }, []);


   return (
    <div className="posts-container">
       {posts.map((post) => {
          return (
             <div className="post-card" key={post.id}>
                <p className="post-body">{post.program_time} {post._start}{post._stop}{post._report}</p>
             </div>
          );
       })}
    </div>
    );
 };

export default AppPage
