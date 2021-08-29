import React from 'react'
import { Nav } from 'react-bootstrap'

const Navbar = () => {
    return (
        <>
        <Nav className="justify-content-center">
            <Nav.Item>
                <Nav.Link href="/">Home</Nav.Link>
            </Nav.Item>
            <Nav.Item>
                <Nav.Link eventKey="">List</Nav.Link>
            </Nav.Item>
            <Nav.Item>
                <Nav.Link eventKey="">Documentation</Nav.Link>
            </Nav.Item>
        </Nav> 
        </>
    )
}

export default Navbar
