--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: blogger; Type: TABLE; Schema: public; Owner: zakov
--

CREATE TABLE public.blogger (
    id integer NOT NULL,
    first_name character varying(100),
    email character varying(100)
);


ALTER TABLE public.blogger OWNER TO zakov;

--
-- Name: blogger_id_seq; Type: SEQUENCE; Schema: public; Owner: zakov
--

CREATE SEQUENCE public.blogger_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blogger_id_seq OWNER TO zakov;

--
-- Name: blogger_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zakov
--

ALTER SEQUENCE public.blogger_id_seq OWNED BY public.blogger.id;


--
-- Name: post; Type: TABLE; Schema: public; Owner: zakov
--

CREATE TABLE public.post (
    id integer NOT NULL,
    title character varying(100),
    body text,
    blogger_id integer,
    created_at date
);


ALTER TABLE public.post OWNER TO zakov;

--
-- Name: post_id_seq; Type: SEQUENCE; Schema: public; Owner: zakov
--

CREATE SEQUENCE public.post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.post_id_seq OWNER TO zakov;

--
-- Name: post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zakov
--

ALTER SEQUENCE public.post_id_seq OWNED BY public.post.id;


--
-- Name: blogger id; Type: DEFAULT; Schema: public; Owner: zakov
--

ALTER TABLE ONLY public.blogger ALTER COLUMN id SET DEFAULT nextval('public.blogger_id_seq'::regclass);


--
-- Name: post id; Type: DEFAULT; Schema: public; Owner: zakov
--

ALTER TABLE ONLY public.post ALTER COLUMN id SET DEFAULT nextval('public.post_id_seq'::regclass);


--
-- Data for Name: blogger; Type: TABLE DATA; Schema: public; Owner: zakov
--

COPY public.blogger (id, first_name, email) FROM stdin;
1	blogger1	\N
2	blogger2	\N
3	blogger3	\N
5	\N	n@gmail.com
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: zakov
--

COPY public.post (id, title, body, blogger_id, created_at) FROM stdin;
1	first post	some text	1	2000-12-02
2	second post	some text	2	2022-12-12
3	third post	some text	3	2024-01-01
7	4 post	some text	1	2045-12-08
8	5 post	some text	2	2032-12-12
9	6 post	some text	3	2024-11-01
10	7 post	some text	1	2345-12-08
11	8 post	some text	2	2232-12-12
12	9 post	some text	3	2824-11-01
\.


--
-- Name: blogger_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zakov
--

SELECT pg_catalog.setval('public.blogger_id_seq', 7, true);


--
-- Name: post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zakov
--

SELECT pg_catalog.setval('public.post_id_seq', 12, true);


--
-- Name: blogger blogger_pkey; Type: CONSTRAINT; Schema: public; Owner: zakov
--

ALTER TABLE ONLY public.blogger
    ADD CONSTRAINT blogger_pkey PRIMARY KEY (id);


--
-- Name: blogger email_unq; Type: CONSTRAINT; Schema: public; Owner: zakov
--

ALTER TABLE ONLY public.blogger
    ADD CONSTRAINT email_unq UNIQUE (email);


--
-- Name: post post_pkey; Type: CONSTRAINT; Schema: public; Owner: zakov
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (id);


--
-- Name: post fk_post_blogger; Type: FK CONSTRAINT; Schema: public; Owner: zakov
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT fk_post_blogger FOREIGN KEY (blogger_id) REFERENCES public.blogger(id);


--
-- PostgreSQL database dump complete
--

