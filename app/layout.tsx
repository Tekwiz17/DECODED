import type { Metadata } from 'next';
import './globals.css';
export const metadata:Metadata={title:'DECODED · Small lessons. Big lightbulb moments.',description:'New York Regents study paths. Short lessons, interactive models, vocabulary and released exam practice with Byte.',icons:{icon:'/favicon.svg'}};
export default function Layout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}
