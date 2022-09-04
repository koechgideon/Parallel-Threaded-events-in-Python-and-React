import React, {useState, useEffect} from 'react'

const AppPage = () => {
   const [posts, setPosts] = useState([]);
   useEffect(() => {
      fetch('http://127.0.0.1:8000/display/')
         .then((response) => response.json())
         .then((data) => {
            console.log(data);
            setPosts(data);
         })
         .catch((err) => {
            console.log(err.message);
         });
   }, []);


   return (
    <div className="posts-container">
       {posts.map((post) => {
          return (
             <div className="post-card" key={post.id}>
                <p className="post-body">{post.program_time}-start {post._start} servers{post._stop}{post._report}</p>
             </div>
          );
       })}
    </div>
    );
 };

export default AppPage
