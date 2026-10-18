import type { Metadata } from 'next';
import './globals.css';
export const metadata:Metadata={title:'DECODED · Small lessons. Big lightbulb moments.',description:'Make Biology click. Learn with Byte, your computer companion, through short lessons, animated models, and practice.',icons:{icon:'/favicon.svg'}};
export default function Layout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}
