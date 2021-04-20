import React, {useState} from 'react';
import {Collapse, Nav, Navbar, NavbarBrand, NavbarToggler, NavItem, NavLink} from 'reactstrap';

const MyNavbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const toggle = () => setIsOpen(!isOpen);

  return (
    <div>
      <Navbar color="light" light expand="md">
        <NavbarBrand href="/">aweffr的小站</NavbarBrand>
        <NavbarToggler onClick={toggle}/>
        <Collapse isOpen={isOpen} navbar>
          <Nav className="mr-auto" navbar>
            <NavItem>
              <NavLink href="/blogs/">随笔</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/study/">学习</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/archives/">归档</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/todo/">todo清单</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/tweets/">碎碎念</NavLink>
            </NavItem>
          </Nav>
          <Nav navbar>
            <NavItem>
              <NavLink href="/tools/">工具箱</NavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
}

export default MyNavbar;
