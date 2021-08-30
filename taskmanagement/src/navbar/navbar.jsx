import React from 'react'
import { Nav, NavDropdown } from 'react-bootstrap'

const Navbar = () => {
    return (
        <>
        <Nav className="justify-content-center">
            <Nav.Item>
                <Nav.Link href="/">Home</Nav.Link>
            </Nav.Item>
            <Nav.Item>
                <NavDropdown title="List" id="basic-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1">Clients</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.2">Subtasks</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.3">Tasks</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.4">Projects</NavDropdown.Item>

                </NavDropdown>
            </Nav.Item>
            <Nav.Item>
                <NavDropdown title="Documentation" id="basic-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1">Swagger</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.2">Redoc</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.3">API</NavDropdown.Item>
                </NavDropdown>
            </Nav.Item>
        </Nav> 
        </>
    )
}

export default Navbar
