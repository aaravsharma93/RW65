--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE yardman_admin;
ALTER ROLE yardman_admin WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'md5516b46e6b61307d1a6b1c6b53a0a466f';




--
-- PostgreSQL database cluster dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.7
-- Dumped by pg_dump version 12.7 (Ubuntu 12.7-0ubuntu0.20.10.1)

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
-- Name: auth_group; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO yardman_admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO yardman_admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO yardman_admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO yardman_admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO yardman_admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO yardman_admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO yardman_admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO yardman_admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO yardman_admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO yardman_admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO yardman_admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO yardman_admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO yardman_admin;

--
-- Name: scale_app_devices; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.scale_app_devices (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    ip_addr character varying(100) NOT NULL,
    serial_num character varying(100) NOT NULL,
    mac_addr character varying(100) NOT NULL,
    port integer NOT NULL,
    wx_btn boolean NOT NULL,
    zero_btn boolean NOT NULL,
    tara_btn boolean NOT NULL,
    man_tara_btn boolean NOT NULL,
    x10_btn boolean NOT NULL,
    active boolean NOT NULL,
    certi_num character varying(100) NOT NULL,
    max_weight integer,
    min_weight integer,
    e_d integer,
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL,
    CONSTRAINT scale_app_devices_e_d_check CHECK ((e_d >= 0)),
    CONSTRAINT scale_app_devices_max_weight_check CHECK ((max_weight >= 0)),
    CONSTRAINT scale_app_devices_min_weight_check CHECK ((min_weight >= 0)),
    CONSTRAINT scale_app_devices_port_check CHECK ((port >= 0))
);


ALTER TABLE public.scale_app_devices OWNER TO yardman_admin;

--
-- Name: scale_app_devices_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.scale_app_devices_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.scale_app_devices_id_seq OWNER TO yardman_admin;

--
-- Name: scale_app_devices_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.scale_app_devices_id_seq OWNED BY public.scale_app_devices.id;


--
-- Name: scale_app_transaction; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.scale_app_transaction (
    trans_id integer NOT NULL,
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL,
    tara numeric(10,2) NOT NULL,
    net_weight numeric(10,2) NOT NULL,
    device_id integer NOT NULL
);


ALTER TABLE public.scale_app_transaction OWNER TO yardman_admin;

--
-- Name: scale_app_transaction_trans_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.scale_app_transaction_trans_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.scale_app_transaction_trans_id_seq OWNER TO yardman_admin;

--
-- Name: scale_app_transaction_trans_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.scale_app_transaction_trans_id_seq OWNED BY public.scale_app_transaction.trans_id;


--
-- Name: yard_article; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_article (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(250),
    short_name character varying(40),
    entry_weight integer,
    balance_weight integer,
    outgoing_weight integer,
    price1 integer,
    price2 numeric(10,2),
    price3 numeric(10,2),
    price4 numeric(10,2),
    price5 numeric(10,2),
    discount character varying(100),
    "group" integer NOT NULL,
    vat numeric(10,2),
    minimum_amount integer,
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL,
    avv_num character varying(250),
    account character varying(250),
    cost_center character varying(250),
    unit character varying(250),
    min_quantity integer,
    revenue_group character varying(250),
    revenue_account character varying(250),
    list_price_net numeric(10,2),
    ean character varying(250),
    supplier_id integer,
    ware_house_id integer,
    yard_id integer,
    CONSTRAINT yard_article_group_check CHECK (("group" >= 0)),
    CONSTRAINT yard_article_min_quantity_check CHECK ((min_quantity >= 0))
);


ALTER TABLE public.yard_article OWNER TO yardman_admin;

--
-- Name: yard_article_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_article_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_article_id_seq OWNER TO yardman_admin;

--
-- Name: yard_article_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_article_id_seq OWNED BY public.yard_article.id;


--
-- Name: yard_article_meta; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_article_meta (
    id integer NOT NULL,
    entry_weight numeric(10,3),
    balance_weight numeric(10,3),
    outgoing_weight numeric(10,3),
    article_id integer,
    yard_id integer NOT NULL
);


ALTER TABLE public.yard_article_meta OWNER TO yardman_admin;

--
-- Name: yard_article_meta_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_article_meta_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_article_meta_id_seq OWNER TO yardman_admin;

--
-- Name: yard_article_meta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_article_meta_id_seq OWNED BY public.yard_article_meta.id;


--
-- Name: yard_buildingsite; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_buildingsite (
    id integer NOT NULL,
    name character varying(100),
    short_name character varying(40),
    place character varying(100),
    street character varying(100),
    pin character varying(100),
    infotext character varying(100) NOT NULL,
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL
);


ALTER TABLE public.yard_buildingsite OWNER TO yardman_admin;

--
-- Name: yard_buildingsite_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_buildingsite_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_buildingsite_id_seq OWNER TO yardman_admin;

--
-- Name: yard_buildingsite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_buildingsite_id_seq OWNED BY public.yard_buildingsite.id;


--
-- Name: yard_combination; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_combination (
    id integer NOT NULL,
    ident character varying(40) NOT NULL,
    short_name character varying(40),
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL,
    article_id integer,
    building_site_id integer,
    customer_id integer,
    forwarders_id integer,
    supplier_id integer,
    vehicle_id integer,
    yard_id integer
);


ALTER TABLE public.yard_combination OWNER TO yardman_admin;

--
-- Name: yard_combination_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_combination_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_combination_id_seq OWNER TO yardman_admin;

--
-- Name: yard_combination_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_combination_id_seq OWNED BY public.yard_combination.id;


--
-- Name: yard_container; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_container (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    container_type character varying(40),
    "group" integer,
    container_weight numeric(10,2) NOT NULL,
    volume character varying(40),
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL,
    last_site_id integer,
    container_number integer,
    hazard_warnings character varying(200),
    maximum_gross_weight numeric(10,2) NOT NULL,
    next_exam date,
    payload_container_volume character varying(40),
    tare_weight numeric(10,2),
    waste_type character varying(50),
    CONSTRAINT yard_container_container_number_check CHECK ((container_number >= 0)),
    CONSTRAINT yard_container_group_check CHECK (("group" >= 0))
);


ALTER TABLE public.yard_container OWNER TO yardman_admin;

--
-- Name: yard_container_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_container_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_container_id_seq OWNER TO yardman_admin;

--
-- Name: yard_container_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_container_id_seq OWNED BY public.yard_container.id;


--
-- Name: yard_customer; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_customer (
    id integer NOT NULL,
    name character varying(40) NOT NULL,
    firstname character varying(40),
    company character varying(40),
    salutation character varying(10) NOT NULL,
    addition1 character varying(40),
    addition2 character varying(40),
    addition3 character varying(40),
    post_office_box character varying(40),
    description character varying(250),
    street character varying(250),
    pin character varying(10),
    fax character varying(15),
    place character varying(100),
    website character varying(100),
    cost_centre integer,
    country character varying(100),
    contact_person1_email character varying(40),
    contact_person2_email character varying(40),
    contact_person3_email character varying(40),
    contact_person1_phone character varying(40),
    contact_person2_phone character varying(40),
    contact_person3_phone character varying(40),
    diff_invoice_recipient character varying(40),
    customer_type character varying(40),
    price_group character varying(10) NOT NULL,
    classification character varying(40),
    sector character varying(40),
    company_size character varying(40),
    area character varying(40),
    private_person boolean NOT NULL,
    document_lock boolean NOT NULL,
    payment_block boolean NOT NULL,
    delivery_terms character varying(10) NOT NULL,
    special_discount numeric(10,2),
    debitor_number integer,
    dunning character varying(10),
    perm_street character varying(100),
    perm_pin character varying(10),
    perm_place character varying(100),
    perm_country character varying(100),
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL,
    warehouse_id integer,
    CONSTRAINT yard_customer_cost_centre_check CHECK ((cost_centre >= 0)),
    CONSTRAINT yard_customer_debitor_number_check CHECK ((debitor_number >= 0))
);


ALTER TABLE public.yard_customer OWNER TO yardman_admin;

--
-- Name: yard_customer_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_customer_id_seq OWNER TO yardman_admin;

--
-- Name: yard_customer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_customer_id_seq OWNED BY public.yard_customer.id;


--
-- Name: yard_delivery_note; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_delivery_note (
    id integer NOT NULL,
    lfd_nr character varying(100) NOT NULL,
    file_name character varying(100) NOT NULL,
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL
);


ALTER TABLE public.yard_delivery_note OWNER TO yardman_admin;

--
-- Name: yard_delivery_note_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_delivery_note_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_delivery_note_id_seq OWNER TO yardman_admin;

--
-- Name: yard_delivery_note_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_delivery_note_id_seq OWNED BY public.yard_delivery_note.id;


--
-- Name: yard_forwarders; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_forwarders (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    firstname character varying(100),
    second_name character varying(100),
    street character varying(100),
    pin character varying(10),
    telephone character varying(15),
    place character varying(100),
    country character varying(100),
    contact_person character varying(100),
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL
);


ALTER TABLE public.yard_forwarders OWNER TO yardman_admin;

--
-- Name: yard_forwarders_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_forwarders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_forwarders_id_seq OWNER TO yardman_admin;

--
-- Name: yard_forwarders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_forwarders_id_seq OWNED BY public.yard_forwarders.id;


--
-- Name: yard_images_base64; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_images_base64 (
    id integer NOT NULL,
    image1 character varying(100),
    image2 character varying(100),
    image3 character varying(100),
    transaction_id integer
);


ALTER TABLE public.yard_images_base64 OWNER TO yardman_admin;

--
-- Name: yard_images_base64_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_images_base64_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_images_base64_id_seq OWNER TO yardman_admin;

--
-- Name: yard_images_base64_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_images_base64_id_seq OWNED BY public.yard_images_base64.id;


--
-- Name: yard_logo; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_logo (
    id integer NOT NULL,
    heading character varying(100)
);


ALTER TABLE public.yard_logo OWNER TO yardman_admin;

--
-- Name: yard_logo_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_logo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_logo_id_seq OWNER TO yardman_admin;

--
-- Name: yard_logo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_logo_id_seq OWNED BY public.yard_logo.id;


--
-- Name: yard_selectcamera; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_selectcamera (
    id integer NOT NULL,
    yes boolean NOT NULL
);


ALTER TABLE public.yard_selectcamera OWNER TO yardman_admin;

--
-- Name: yard_selectcamera_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_selectcamera_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_selectcamera_id_seq OWNER TO yardman_admin;

--
-- Name: yard_selectcamera_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_selectcamera_id_seq OWNED BY public.yard_selectcamera.id;


--
-- Name: yard_settings; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_settings (
    id integer NOT NULL,
    name character varying(40),
    customer character varying(40),
    supplier character varying(40),
    article character varying(40),
    show_article boolean NOT NULL,
    show_supplier boolean NOT NULL,
    show_yard boolean NOT NULL,
    show_forwarders boolean NOT NULL,
    show_storage boolean NOT NULL,
    show_building_site boolean NOT NULL,
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL,
    read_number_from_camera boolean NOT NULL,
    language character varying(40),
    yard_id integer NOT NULL
);


ALTER TABLE public.yard_settings OWNER TO yardman_admin;

--
-- Name: yard_settings_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_settings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_settings_id_seq OWNER TO yardman_admin;

--
-- Name: yard_settings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_settings_id_seq OWNED BY public.yard_settings.id;


--
-- Name: yard_supplier; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_supplier (
    id integer NOT NULL,
    supplier_name character varying(100) NOT NULL,
    name character varying(40),
    first_name character varying(40),
    street character varying(100),
    pin character varying(10),
    fax character varying(15),
    place character varying(100),
    infotext character varying(100),
    salutation character varying(10) NOT NULL,
    addition1 character varying(40),
    addition2 character varying(40),
    addition3 character varying(40),
    post_office_box character varying(40),
    country character varying(100),
    contact_person1_email character varying(40),
    contact_person2_email character varying(40),
    contact_person3_email character varying(40),
    contact_person1_phone character varying(40),
    contact_person2_phone character varying(40),
    contact_person3_phone character varying(40),
    website character varying(100),
    cost_centre integer,
    creditor_number bigint,
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL,
    warehouse_id integer,
    CONSTRAINT yard_supplier_cost_centre_check CHECK ((cost_centre >= 0))
);


ALTER TABLE public.yard_supplier OWNER TO yardman_admin;

--
-- Name: yard_supplier_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_supplier_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_supplier_id_seq OWNER TO yardman_admin;

--
-- Name: yard_supplier_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_supplier_id_seq OWNED BY public.yard_supplier.id;


--
-- Name: yard_transaction; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_transaction (
    id integer NOT NULL,
    first_weight numeric(10,0) NOT NULL,
    second_weight numeric(10,0) NOT NULL,
    net_weight numeric(10,0) NOT NULL,
    total_price numeric(10,0),
    lfd_nr character varying(40),
    firstw_date_time timestamp with time zone,
    secondw_date_time timestamp with time zone,
    firstw_alibi_nr character varying(40),
    secondw_alibi_nr character varying(40),
    vehicle_weight_flag integer,
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL,
    trans_flag integer,
    price_per_item numeric(10,2),
    article_id integer,
    customer_id integer,
    supplier_id integer,
    vehicle_id integer,
    yard_id integer,
    vehicle_second_weight_flag integer,
    CONSTRAINT yard_transaction_trans_flag_check CHECK ((trans_flag >= 0))
);


ALTER TABLE public.yard_transaction OWNER TO yardman_admin;

--
-- Name: yard_transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_transaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_transaction_id_seq OWNER TO yardman_admin;

--
-- Name: yard_transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_transaction_id_seq OWNED BY public.yard_transaction.id;


--
-- Name: yard_user; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    role character varying(30) NOT NULL,
    yard_id integer
);


ALTER TABLE public.yard_user OWNER TO yardman_admin;

--
-- Name: yard_user_groups; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.yard_user_groups OWNER TO yardman_admin;

--
-- Name: yard_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_user_groups_id_seq OWNER TO yardman_admin;

--
-- Name: yard_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_user_groups_id_seq OWNED BY public.yard_user_groups.id;


--
-- Name: yard_user_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_user_id_seq OWNER TO yardman_admin;

--
-- Name: yard_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_user_id_seq OWNED BY public.yard_user.id;


--
-- Name: yard_user_user_permissions; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.yard_user_user_permissions OWNER TO yardman_admin;

--
-- Name: yard_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_user_user_permissions_id_seq OWNER TO yardman_admin;

--
-- Name: yard_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_user_user_permissions_id_seq OWNED BY public.yard_user_user_permissions.id;


--
-- Name: yard_vehicle; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_vehicle (
    id integer NOT NULL,
    license_plate character varying(100),
    license_plate2 character varying(100),
    "group" integer,
    country character varying(100),
    telephone character varying(20),
    vehicle_weight integer,
    vehicle_weight_id character varying(100),
    taken integer,
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL,
    vehicle_type character varying(10),
    cost_center character varying(100),
    owner character varying(100),
    driver_name character varying(100),
    trailor_weight numeric(10,0) NOT NULL,
    forwarder_id integer,
    vehicle_weight2 integer,
    vehicle_weight_date date,
    vehicle_weight_time time without time zone,
    CONSTRAINT yard_vehicle_group_check CHECK (("group" >= 0)),
    CONSTRAINT yard_vehicle_taken_check CHECK ((taken >= 0))
);


ALTER TABLE public.yard_vehicle OWNER TO yardman_admin;

--
-- Name: yard_vehicle_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_vehicle_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_vehicle_id_seq OWNER TO yardman_admin;

--
-- Name: yard_vehicle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_vehicle_id_seq OWNED BY public.yard_vehicle.id;


--
-- Name: yard_warehouse; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_warehouse (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    stock_designation character varying(100),
    stock_number character varying(100),
    stock_item boolean NOT NULL,
    locked_warehouse boolean NOT NULL,
    ordered boolean NOT NULL,
    production character varying(100),
    reserved character varying(100),
    available integer,
    total_stock integer,
    store integer,
    outsource integer,
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL,
    storage_location character varying(100),
    warehouse_street character varying(100),
    minimum_quantity integer,
    CONSTRAINT yard_warehouse_available_check CHECK ((available >= 0)),
    CONSTRAINT yard_warehouse_minimum_quantity_check CHECK ((minimum_quantity >= 0)),
    CONSTRAINT yard_warehouse_outsource_check CHECK ((outsource >= 0)),
    CONSTRAINT yard_warehouse_store_check CHECK ((store >= 0)),
    CONSTRAINT yard_warehouse_total_stock_check CHECK ((total_stock >= 0))
);


ALTER TABLE public.yard_warehouse OWNER TO yardman_admin;

--
-- Name: yard_warehouse_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_warehouse_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_warehouse_id_seq OWNER TO yardman_admin;

--
-- Name: yard_warehouse_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_warehouse_id_seq OWNED BY public.yard_warehouse.id;


--
-- Name: yard_yard_list; Type: TABLE; Schema: public; Owner: yardman_admin
--

CREATE TABLE public.yard_yard_list (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    street character varying(40),
    pin character varying(10),
    place character varying(40),
    country character varying(40),
    telephone character varying(15),
    email character varying(40),
    created_date_time timestamp with time zone NOT NULL,
    updated_date_time timestamp with time zone NOT NULL
);


ALTER TABLE public.yard_yard_list OWNER TO yardman_admin;

--
-- Name: yard_yard_list_id_seq; Type: SEQUENCE; Schema: public; Owner: yardman_admin
--

CREATE SEQUENCE public.yard_yard_list_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yard_yard_list_id_seq OWNER TO yardman_admin;

--
-- Name: yard_yard_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yardman_admin
--

ALTER SEQUENCE public.yard_yard_list_id_seq OWNED BY public.yard_yard_list.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: scale_app_devices id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.scale_app_devices ALTER COLUMN id SET DEFAULT nextval('public.scale_app_devices_id_seq'::regclass);


--
-- Name: scale_app_transaction trans_id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.scale_app_transaction ALTER COLUMN trans_id SET DEFAULT nextval('public.scale_app_transaction_trans_id_seq'::regclass);


--
-- Name: yard_article id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_article ALTER COLUMN id SET DEFAULT nextval('public.yard_article_id_seq'::regclass);


--
-- Name: yard_article_meta id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_article_meta ALTER COLUMN id SET DEFAULT nextval('public.yard_article_meta_id_seq'::regclass);


--
-- Name: yard_buildingsite id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_buildingsite ALTER COLUMN id SET DEFAULT nextval('public.yard_buildingsite_id_seq'::regclass);


--
-- Name: yard_combination id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_combination ALTER COLUMN id SET DEFAULT nextval('public.yard_combination_id_seq'::regclass);


--
-- Name: yard_container id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_container ALTER COLUMN id SET DEFAULT nextval('public.yard_container_id_seq'::regclass);


--
-- Name: yard_customer id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_customer ALTER COLUMN id SET DEFAULT nextval('public.yard_customer_id_seq'::regclass);


--
-- Name: yard_delivery_note id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_delivery_note ALTER COLUMN id SET DEFAULT nextval('public.yard_delivery_note_id_seq'::regclass);


--
-- Name: yard_forwarders id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_forwarders ALTER COLUMN id SET DEFAULT nextval('public.yard_forwarders_id_seq'::regclass);


--
-- Name: yard_images_base64 id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_images_base64 ALTER COLUMN id SET DEFAULT nextval('public.yard_images_base64_id_seq'::regclass);


--
-- Name: yard_logo id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_logo ALTER COLUMN id SET DEFAULT nextval('public.yard_logo_id_seq'::regclass);


--
-- Name: yard_selectcamera id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_selectcamera ALTER COLUMN id SET DEFAULT nextval('public.yard_selectcamera_id_seq'::regclass);


--
-- Name: yard_settings id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_settings ALTER COLUMN id SET DEFAULT nextval('public.yard_settings_id_seq'::regclass);


--
-- Name: yard_supplier id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_supplier ALTER COLUMN id SET DEFAULT nextval('public.yard_supplier_id_seq'::regclass);


--
-- Name: yard_transaction id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_transaction ALTER COLUMN id SET DEFAULT nextval('public.yard_transaction_id_seq'::regclass);


--
-- Name: yard_user id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user ALTER COLUMN id SET DEFAULT nextval('public.yard_user_id_seq'::regclass);


--
-- Name: yard_user_groups id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user_groups ALTER COLUMN id SET DEFAULT nextval('public.yard_user_groups_id_seq'::regclass);


--
-- Name: yard_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.yard_user_user_permissions_id_seq'::regclass);


--
-- Name: yard_vehicle id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_vehicle ALTER COLUMN id SET DEFAULT nextval('public.yard_vehicle_id_seq'::regclass);


--
-- Name: yard_warehouse id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_warehouse ALTER COLUMN id SET DEFAULT nextval('public.yard_warehouse_id_seq'::regclass);


--
-- Name: yard_yard_list id; Type: DEFAULT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_yard_list ALTER COLUMN id SET DEFAULT nextval('public.yard_yard_list_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add user	6	add_user
22	Can change user	6	change_user
23	Can delete user	6	delete_user
24	Can view user	6	view_user
25	Can add images_base64	7	add_images_base64
26	Can change images_base64	7	change_images_base64
27	Can delete images_base64	7	delete_images_base64
28	Can view images_base64	7	view_images_base64
29	Can add article	8	add_article
30	Can change article	8	change_article
31	Can delete article	8	delete_article
32	Can view article	8	view_article
33	Can add article_meta	9	add_article_meta
34	Can change article_meta	9	change_article_meta
35	Can delete article_meta	9	delete_article_meta
36	Can view article_meta	9	view_article_meta
37	Can add building site	10	add_buildingsite
38	Can change building site	10	change_buildingsite
39	Can delete building site	10	delete_buildingsite
40	Can view building site	10	view_buildingsite
41	Can add delivery_note	11	add_delivery_note
42	Can change delivery_note	11	change_delivery_note
43	Can delete delivery_note	11	delete_delivery_note
44	Can view delivery_note	11	view_delivery_note
45	Can add vehicle	12	add_vehicle
46	Can change vehicle	12	change_vehicle
47	Can delete vehicle	12	delete_vehicle
48	Can view vehicle	12	view_vehicle
49	Can add combination	13	add_combination
50	Can change combination	13	change_combination
51	Can delete combination	13	delete_combination
52	Can view combination	13	view_combination
53	Can add customer	14	add_customer
54	Can change customer	14	change_customer
55	Can delete customer	14	delete_customer
56	Can view customer	14	view_customer
57	Can add supplier	15	add_supplier
58	Can change supplier	15	change_supplier
59	Can delete supplier	15	delete_supplier
60	Can view supplier	15	view_supplier
61	Can add forwarders	16	add_forwarders
62	Can change forwarders	16	change_forwarders
63	Can delete forwarders	16	delete_forwarders
64	Can view forwarders	16	view_forwarders
65	Can add transaction	17	add_transaction
66	Can change transaction	17	change_transaction
67	Can delete transaction	17	delete_transaction
68	Can view transaction	17	view_transaction
69	Can add yard_list	18	add_yard_list
70	Can change yard_list	18	change_yard_list
71	Can delete yard_list	18	delete_yard_list
72	Can view yard_list	18	view_yard_list
73	Can add settings	19	add_settings
74	Can change settings	19	change_settings
75	Can delete settings	19	delete_settings
76	Can view settings	19	view_settings
77	Can add container	20	add_container
78	Can change container	20	change_container
79	Can delete container	20	delete_container
80	Can view container	20	view_container
81	Can add warehouse	21	add_warehouse
82	Can change warehouse	21	change_warehouse
83	Can delete warehouse	21	delete_warehouse
84	Can view warehouse	21	view_warehouse
85	Can add logo	22	add_logo
86	Can change logo	22	change_logo
87	Can delete logo	22	delete_logo
88	Can view logo	22	view_logo
89	Can add select camera	23	add_selectcamera
90	Can change select camera	23	change_selectcamera
91	Can delete select camera	23	delete_selectcamera
92	Can view select camera	23	view_selectcamera
93	Can add devices	24	add_devices
94	Can change devices	24	change_devices
95	Can delete devices	24	delete_devices
96	Can view devices	24	view_devices
97	Can add transaction	25	add_transaction
98	Can change transaction	25	change_transaction
99	Can delete transaction	25	delete_transaction
100	Can view transaction	25	view_transaction
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	yard	user
7	yard	images_base64
8	yard	article
9	yard	article_meta
10	yard	buildingsite
11	yard	delivery_note
12	yard	vehicle
13	yard	combination
14	yard	customer
15	yard	supplier
16	yard	forwarders
17	yard	transaction
18	yard	yard_list
19	yard	settings
20	yard	container
21	yard	warehouse
22	yard	logo
23	yard	selectcamera
24	scale_app	devices
25	scale_app	transaction
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-05-27 17:41:42.665551+00
2	contenttypes	0002_remove_content_type_name	2021-05-27 17:41:42.704309+00
3	auth	0001_initial	2021-05-27 17:41:42.815915+00
4	auth	0002_alter_permission_name_max_length	2021-05-27 17:41:44.471786+00
5	auth	0003_alter_user_email_max_length	2021-05-27 17:41:44.768064+00
6	auth	0004_alter_user_username_opts	2021-05-27 17:41:44.940188+00
7	auth	0005_alter_user_last_login_null	2021-05-27 17:41:45.105049+00
8	auth	0006_require_contenttypes_0002	2021-05-27 17:41:45.258855+00
9	auth	0007_alter_validators_add_error_messages	2021-05-27 17:41:45.430397+00
10	auth	0008_alter_user_username_max_length	2021-05-27 17:41:45.603119+00
11	auth	0009_alter_user_last_name_max_length	2021-05-27 17:41:45.769413+00
12	auth	0010_alter_group_name_max_length	2021-05-27 17:41:45.934197+00
13	auth	0011_update_proxy_permissions	2021-05-27 17:41:46.098959+00
14	auth	0012_alter_user_first_name_max_length	2021-05-27 17:41:46.271981+00
15	yard	0001_initial	2021-05-27 17:41:48.337108+00
16	admin	0001_initial	2021-05-27 17:41:49.045482+00
17	admin	0002_logentry_remove_auto_add	2021-05-27 17:41:49.122418+00
18	admin	0003_logentry_add_action_flag_choices	2021-05-27 17:41:49.168341+00
19	scale_app	0001_initial	2021-05-27 17:41:49.496017+00
20	sessions	0001_initial	2021-05-27 17:41:49.570543+00
21	yard	0002_auto_20210412_1022	2021-05-27 17:41:49.905934+00
22	yard	0003_auto_20210422_0932	2021-05-27 17:41:50.930194+00
23	yard	0004_auto_20210425_2224	2021-05-27 17:41:51.341896+00
24	yard	0005_warehouse_minimum_quantity	2021-05-27 17:41:51.390941+00
25	yard	0006_auto_20210429_0955	2021-05-27 17:41:51.473245+00
26	yard	0007_auto_20210505_1114	2021-05-27 17:41:52.193637+00
27	yard	0008_auto_20210506_0902	2021-05-27 17:41:54.044334+00
28	yard	0009_selectcamera	2021-05-27 17:41:54.102725+00
29	yard	0010_auto_20210507_0904	2021-05-27 17:41:54.159364+00
30	yard	0011_auto_20210526_0744	2021-05-27 17:41:54.44972+00
31	yard	0011_auto_20210515_0923	2021-06-01 06:15:02.602821+00
32	yard	0012_auto_20210602_1233	2021-06-02 10:33:15.739632+00
33	yard	0013_auto_20210603_1004	2021-06-03 08:04:59.27335+00
34	yard	0014_transaction_vehicle_second_weight_flag	2021-06-03 11:44:02.862489+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
1p1fal4yytf45m5hs7rkfdkjjd8uucy2	.eJxVjEEOwiAQRe_C2hDKAAWX7nsGMgOMrZqSlHZlvLtt0oVu_3vvv0XEbR3j1soSpyyuohOX340wPct8gPzA-V5lqvO6TCQPRZ60yaHm8rqd7t_BiG3c64TKEjmj-xC8Vqwh9-ycV4ZSJoMMXJLTANZmBmDFCbTHQKGobpfF5wvkPjf8:1loR4g:_06G7wtVUjdpZO48jdIk0-J2UtnbPB4bFqUGRAkgZOE	2021-06-16 13:38:22.50117+00
cs2befmsjxvqe3pnieb7w2j7q0cfjkxw	.eJxVkMtugzAQRf_F6woRDATYNduq32CN7TG4MXbkh6Kq6r93iFAadqNz7lxp5ocJKHkRJWEUVrOJndjbK5Ogrug3ob_Az6FSwedoZbVFqt2m6jNodJc9eyhYIC20raDupOzb5jyOQ1Obhuuz6fuhbqXSsgXDDaq-4bzrtOHc1EbxZoBRjlifKEylqqQcVozU9lG8RkKp3G7OPtAFSKNzG4aYraJpYu80XdFt0SXcxVPkWHBn_x0v8BuiPgAT4p0YxnRcziHCfCyUxTpt_SySzU8TEbTwZZX0EhPDKhTQKcAmAy6Rd_Tc8mhidNnvHw5gjd0:1lollw:BOAw7WrSIFTS8ubxc1Urm9g6qzbeiWxvIDKuOvMcTe0	2021-06-17 11:44:24.765904+00
ha3w52rq8wwkb7omh4n649romibluwc6	.eJxVkMtugzAQRf_F6woRDCRk1WZb9RussT0OboyN_BCqqv57h4imYWONzrm-0sw3wwmsY2cGerL-9f5WKkzshc2Q0hKi_pOEBJQ8ipIwCrvyw55JUDf0q9Cf4K-BinyOVlZrpNpsqj6CRnfZsruCEdJIvxXUnZR92xyH4dTUpuH6aPr-VLdSadmC4QZV33DeddpwbmqjeHOCQQ5YHyhMpaqkHCaM1PZevEZCqcyzs3d0AdLo3IohZqtoOrM3mm7o1ugYFvEQORbc2H_HE_yC9UhPwIS4EMOY9p9ziHDdF8pinbb-KpLNDxMRtPBlknQSE8MkFNAqwM4GXCLv6Ljl3sRos59fjmCc_A:1lomU2:Q-_tVwu6ZJNh3j-9Kyj717ebzCWzFToxYm_YTUqUnnA	2021-06-17 12:29:58.357143+00
\.


--
-- Data for Name: scale_app_devices; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.scale_app_devices (id, name, ip_addr, serial_num, mac_addr, port, wx_btn, zero_btn, tara_btn, man_tara_btn, x10_btn, active, certi_num, max_weight, min_weight, e_d, created_date_time, updated_date_time) FROM stdin;
\.


--
-- Data for Name: scale_app_transaction; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.scale_app_transaction (trans_id, created_date_time, updated_date_time, tara, net_weight, device_id) FROM stdin;
\.


--
-- Data for Name: yard_article; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_article (id, name, description, short_name, entry_weight, balance_weight, outgoing_weight, price1, price2, price3, price4, price5, discount, "group", vat, minimum_amount, created_date_time, updated_date_time, avv_num, account, cost_center, unit, min_quantity, revenue_group, revenue_account, list_price_net, ean, supplier_id, ware_house_id, yard_id) FROM stdin;
3	Sand		\N	0	0	\N	\N	\N	\N	\N	\N	\N	1	\N	0	2021-06-03 09:37:51.098885+00	2021-06-03 09:37:51.108396+00	\N	\N	\N	\N	\N	revenue1	\N	\N	\N	\N	\N	1
\.


--
-- Data for Name: yard_article_meta; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_article_meta (id, entry_weight, balance_weight, outgoing_weight, article_id, yard_id) FROM stdin;
\.


--
-- Data for Name: yard_buildingsite; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_buildingsite (id, name, short_name, place, street, pin, infotext, created_date_time, updated_date_time) FROM stdin;
\.


--
-- Data for Name: yard_combination; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_combination (id, ident, short_name, created_date_time, updated_date_time, article_id, building_site_id, customer_id, forwarders_id, supplier_id, vehicle_id, yard_id) FROM stdin;
1	ID auswählen oder neue ID eingeben	\N	2021-06-03 09:20:32.056196+00	2021-06-03 09:20:32.065577+00	\N	\N	\N	\N	\N	\N	1
\.


--
-- Data for Name: yard_container; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_container (id, name, container_type, "group", container_weight, volume, created_date_time, updated_date_time, last_site_id, container_number, hazard_warnings, maximum_gross_weight, next_exam, payload_container_volume, tare_weight, waste_type) FROM stdin;
\.


--
-- Data for Name: yard_customer; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_customer (id, name, firstname, company, salutation, addition1, addition2, addition3, post_office_box, description, street, pin, fax, place, website, cost_centre, country, contact_person1_email, contact_person2_email, contact_person3_email, contact_person1_phone, contact_person2_phone, contact_person3_phone, diff_invoice_recipient, customer_type, price_group, classification, sector, company_size, area, private_person, document_lock, payment_block, delivery_terms, special_discount, debitor_number, dunning, perm_street, perm_pin, perm_place, perm_country, created_date_time, updated_date_time, warehouse_id) FROM stdin;
1	T	Wöhrl	Rüdiger Wöhrl GmbH	Mr	\N	\N	\N	\N	\N		\N	\N		\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	price1	\N	\N	\N	\N	f	f	f	free	\N	\N	\N	\N	\N	\N	\N	2021-06-02 12:41:04.134728+00	2021-06-02 12:54:28.824599+00	\N
\.


--
-- Data for Name: yard_delivery_note; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_delivery_note (id, lfd_nr, file_name, created_date_time, updated_date_time) FROM stdin;
\.


--
-- Data for Name: yard_forwarders; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_forwarders (id, name, firstname, second_name, street, pin, telephone, place, country, contact_person, created_date_time, updated_date_time) FROM stdin;
\.


--
-- Data for Name: yard_images_base64; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_images_base64 (id, image1, image2, image3, transaction_id) FROM stdin;
5				5
4				4
6				6
7				7
8				8
9				9
10				10
11				12
12				13
13				14
14				15
15				16
16				17
17				18
18				19
\.


--
-- Data for Name: yard_logo; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_logo (id, heading) FROM stdin;
1	Rüdiger Wöhrl GmbH Goldbergstr. 1 74629 Pfedelbach
\.


--
-- Data for Name: yard_selectcamera; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_selectcamera (id, yes) FROM stdin;
3	t
\.


--
-- Data for Name: yard_settings; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_settings (id, name, customer, supplier, article, show_article, show_supplier, show_yard, show_forwarders, show_storage, show_building_site, created_date_time, updated_date_time, read_number_from_camera, language, yard_id) FROM stdin;
1	Ali	Kunde	Baustelle	Artikel	t	t	t	t	t	t	2021-06-03 05:51:49.651252+00	2021-06-03 09:55:08.792186+00	f	de	1
\.


--
-- Data for Name: yard_supplier; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_supplier (id, supplier_name, name, first_name, street, pin, fax, place, infotext, salutation, addition1, addition2, addition3, post_office_box, country, contact_person1_email, contact_person2_email, contact_person3_email, contact_person1_phone, contact_person2_phone, contact_person3_phone, website, cost_centre, creditor_number, created_date_time, updated_date_time, warehouse_id) FROM stdin;
\.


--
-- Data for Name: yard_transaction; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_transaction (id, first_weight, second_weight, net_weight, total_price, lfd_nr, firstw_date_time, secondw_date_time, firstw_alibi_nr, secondw_alibi_nr, vehicle_weight_flag, created_date_time, updated_date_time, trans_flag, price_per_item, article_id, customer_id, supplier_id, vehicle_id, yard_id, vehicle_second_weight_flag) FROM stdin;
6	218	218	0	0	\N	1999-12-31 23:00:00+00	2021-06-02 12:53:00+00	0000	133	1	2021-06-02 12:55:39.666842+00	2021-06-02 12:55:39.676506+00	1	0.00	\N	\N	\N	1	1	0
7	218	218	0	0	\N	1999-12-31 23:00:00+00	2021-06-02 12:54:00+00	0000	135	1	2021-06-02 12:56:23.481092+00	2021-06-02 13:02:25.515837+00	1	\N	\N	\N	\N	12	1	0
5	0	218	218	0	\N	1999-12-31 23:00:00+00	2021-06-02 12:47:00+00	0000	130	0	2021-06-02 12:49:30.925565+00	2021-06-02 13:03:06.432412+00	1	0.00	\N	\N	\N	1	1	0
8	218	218	0	0	\N	1999-12-31 23:00:00+00	2021-06-02 13:21:00+00	0000	136	1	2021-06-02 13:23:38.89077+00	2021-06-02 13:23:38.901073+00	1	0.00	\N	\N	\N	1	1	0
11	500	218	282	0	\N	1999-12-31 23:00:00+00	2021-06-03 08:15:00+00	0000	1	2	2021-06-03 08:17:32.395955+00	2021-06-03 08:27:30.083373+00	1	0.00	\N	\N	\N	12	1	0
12	218	218	0	0	\N	1999-12-31 23:00:00+00	2021-06-03 09:17:00+00	0000	8	1	2021-06-03 09:20:01.624401+00	2021-06-03 09:20:01.636058+00	1	\N	\N	\N	\N	13	1	0
13	0	218	218	218	\N	1999-12-31 23:00:00+00	2021-06-03 09:18:00+00	0000	9	0	2021-06-03 09:20:19.066525+00	2021-06-03 09:20:19.075924+00	1	\N	\N	\N	\N	\N	1	0
14	218	0	0	0	\N	2021-06-03 09:18:00+00	2021-06-03 09:18:00+00	10	9	0	2021-06-03 09:20:31.993805+00	2021-06-03 09:20:32.003912+00	0	\N	\N	\N	\N	\N	1	0
4	500	218	0	0	\N	2021-06-02 12:45:00+00	2021-06-02 12:46:00+00	127	128	2	2021-06-02 12:48:03.797295+00	2021-06-03 09:21:49.40392+00	1	\N	\N	1	\N	1	1	0
10	218	218	0	0	\N	1999-12-31 23:00:00+00	2021-06-02 19:08:00+00	0000	139	2	2021-06-02 19:10:21.796458+00	2021-06-03 09:22:24.734738+00	1	\N	\N	\N	\N	13	1	0
15	218	218	0	0	\N	2021-06-03 09:22:00+00	2021-06-03 09:22:00+00	13	14	0	2021-06-03 09:24:24.162761+00	2021-06-03 09:24:36.142296+00	1	\N	\N	\N	\N	12	1	0
16	218	218	0	0	\N	2021-06-01 09:48:00+00	2021-06-03 09:24:00+00	15	16	0	2021-06-03 09:26:16.935055+00	2021-06-03 09:26:30.815639+00	1	\N	\N	\N	\N	1	1	0
17	500	218	282	0	\N	2021-06-03 09:27:00+00	2021-06-03 09:27:00+00	17	19	1	2021-06-03 09:29:16.373154+00	2021-06-03 09:29:47.204344+00	1	\N	\N	\N	\N	12	1	0
18	218	218	0	0	\N	1999-12-31 23:00:00+00	2021-06-03 09:28:00+00	0000	20	1	2021-06-03 09:31:06.286703+00	2021-06-03 09:31:06.296732+00	1	0.00	\N	\N	\N	13	1	0
9	218	218	0	0	\N	1999-12-31 23:00:00+00	2021-06-02 19:04:00+00	0000	137	2	2021-06-02 19:06:59.96178+00	2021-06-03 09:51:50.437824+00	1	0.00	\N	\N	\N	12	1	0
19	300	60	282	282	\N	1999-12-31 23:00:00+00	2021-06-03 09:29:00+00	0000	21	2	2021-06-03 09:31:26.158196+00	2021-06-03 11:44:42.743735+00	1	\N	\N	\N	\N	12	1	2
20	218	218	0	0	\N	2021-06-03 12:06:00+00	2021-06-03 12:07:00+00	22	23	0	2021-06-03 12:08:55.644677+00	2021-06-03 12:09:29.57163+00	1	\N	\N	\N	\N	13	1	0
\.


--
-- Data for Name: yard_user; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_user (id, password, last_login, is_superuser, name, email, date_joined, is_active, is_staff, role, yard_id) FROM stdin;
1	pbkdf2_sha256$216000$8e3y1L7nOQEI$cvrYeJ9km/YVR6taxNbPEIxO6Gn65hD3dvWtcnUdxS0=	2021-06-02 13:38:22.488251+00	t		admin@admin.com	2021-06-02 12:30:55.653554+00	t	t		1
\.


--
-- Data for Name: yard_user_groups; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: yard_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: yard_vehicle; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_vehicle (id, license_plate, license_plate2, "group", country, telephone, vehicle_weight, vehicle_weight_id, taken, created_date_time, updated_date_time, vehicle_type, cost_center, owner, driver_name, trailor_weight, forwarder_id, vehicle_weight2, vehicle_weight_date, vehicle_weight_time) FROM stdin;
12	ÖHR RW 445		\N			500		0	2021-06-02 12:56:16.327887+00	2021-06-03 09:43:31.361241+00		\N	\N	\N	0	\N	\N	\N	\N
13	RW 555		\N	\N	\N	218	\N	\N	2021-06-02 19:09:45.234137+00	2021-06-03 12:09:29.536809+00	\N	\N	\N	\N	0	\N	0	\N	\N
1	ÖHR RW 55		\N			218		0	2021-06-02 12:36:35.794789+00	2021-06-03 09:26:30.777659+00	type1	\N	\N	\N	0	\N	\N	2021-06-01	11:48:00
\.


--
-- Data for Name: yard_warehouse; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_warehouse (id, name, stock_designation, stock_number, stock_item, locked_warehouse, ordered, production, reserved, available, total_stock, store, outsource, created_date_time, updated_date_time, storage_location, warehouse_street, minimum_quantity) FROM stdin;
1	Stuttgart	\N	\N	t	t	t	\N	\N	\N	\N	\N	\N	2021-06-02 13:06:27.339088+00	2021-06-02 13:06:27.339128+00	\N	\N	\N
2	Heilbronn	\N	\N	t	t	t	\N	\N	\N	\N	\N	\N	2021-06-02 13:06:44.51926+00	2021-06-02 13:06:44.519304+00	\N	\N	\N
\.


--
-- Data for Name: yard_yard_list; Type: TABLE DATA; Schema: public; Owner: yardman_admin
--

COPY public.yard_yard_list (id, name, street, pin, place, country, telephone, email, created_date_time, updated_date_time) FROM stdin;
1	Ali	\N	\N	Germany	Germany	\N	\N	2021-06-02 12:31:44.896381+00	2021-06-02 12:31:44.896421+00
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 100, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 25, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 34, true);


--
-- Name: scale_app_devices_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.scale_app_devices_id_seq', 1, false);


--
-- Name: scale_app_transaction_trans_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.scale_app_transaction_trans_id_seq', 1, false);


--
-- Name: yard_article_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_article_id_seq', 8, true);


--
-- Name: yard_article_meta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_article_meta_id_seq', 1, false);


--
-- Name: yard_buildingsite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_buildingsite_id_seq', 1, false);


--
-- Name: yard_combination_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_combination_id_seq', 1, true);


--
-- Name: yard_container_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_container_id_seq', 1, false);


--
-- Name: yard_customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_customer_id_seq', 1, true);


--
-- Name: yard_delivery_note_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_delivery_note_id_seq', 1, false);


--
-- Name: yard_forwarders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_forwarders_id_seq', 1, false);


--
-- Name: yard_images_base64_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_images_base64_id_seq', 18, true);


--
-- Name: yard_logo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_logo_id_seq', 1, true);


--
-- Name: yard_selectcamera_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_selectcamera_id_seq', 3, true);


--
-- Name: yard_settings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_settings_id_seq', 1, true);


--
-- Name: yard_supplier_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_supplier_id_seq', 1, false);


--
-- Name: yard_transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_transaction_id_seq', 20, true);


--
-- Name: yard_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_user_groups_id_seq', 1, false);


--
-- Name: yard_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_user_id_seq', 1, true);


--
-- Name: yard_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_user_user_permissions_id_seq', 1, false);


--
-- Name: yard_vehicle_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_vehicle_id_seq', 13, true);


--
-- Name: yard_warehouse_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_warehouse_id_seq', 2, true);


--
-- Name: yard_yard_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yardman_admin
--

SELECT pg_catalog.setval('public.yard_yard_list_id_seq', 1, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: scale_app_devices scale_app_devices_name_key; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.scale_app_devices
    ADD CONSTRAINT scale_app_devices_name_key UNIQUE (name);


--
-- Name: scale_app_devices scale_app_devices_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.scale_app_devices
    ADD CONSTRAINT scale_app_devices_pkey PRIMARY KEY (id);


--
-- Name: scale_app_transaction scale_app_transaction_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.scale_app_transaction
    ADD CONSTRAINT scale_app_transaction_pkey PRIMARY KEY (trans_id);


--
-- Name: yard_article_meta yard_article_meta_article_id_yard_id_484ce82f_uniq; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_article_meta
    ADD CONSTRAINT yard_article_meta_article_id_yard_id_484ce82f_uniq UNIQUE (article_id, yard_id);


--
-- Name: yard_article_meta yard_article_meta_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_article_meta
    ADD CONSTRAINT yard_article_meta_pkey PRIMARY KEY (id);


--
-- Name: yard_article yard_article_name_yard_id_b6b7be03_uniq; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_article
    ADD CONSTRAINT yard_article_name_yard_id_b6b7be03_uniq UNIQUE (name, yard_id);


--
-- Name: yard_article yard_article_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_article
    ADD CONSTRAINT yard_article_pkey PRIMARY KEY (id);


--
-- Name: yard_buildingsite yard_buildingsite_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_buildingsite
    ADD CONSTRAINT yard_buildingsite_pkey PRIMARY KEY (id);


--
-- Name: yard_combination yard_combination_ident_key; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_combination
    ADD CONSTRAINT yard_combination_ident_key UNIQUE (ident);


--
-- Name: yard_combination yard_combination_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_combination
    ADD CONSTRAINT yard_combination_pkey PRIMARY KEY (id);


--
-- Name: yard_container yard_container_name_key; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_container
    ADD CONSTRAINT yard_container_name_key UNIQUE (name);


--
-- Name: yard_container yard_container_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_container
    ADD CONSTRAINT yard_container_pkey PRIMARY KEY (id);


--
-- Name: yard_customer yard_customer_name_key; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_customer
    ADD CONSTRAINT yard_customer_name_key UNIQUE (name);


--
-- Name: yard_customer yard_customer_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_customer
    ADD CONSTRAINT yard_customer_pkey PRIMARY KEY (id);


--
-- Name: yard_delivery_note yard_delivery_note_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_delivery_note
    ADD CONSTRAINT yard_delivery_note_pkey PRIMARY KEY (id);


--
-- Name: yard_forwarders yard_forwarders_name_key; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_forwarders
    ADD CONSTRAINT yard_forwarders_name_key UNIQUE (name);


--
-- Name: yard_forwarders yard_forwarders_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_forwarders
    ADD CONSTRAINT yard_forwarders_pkey PRIMARY KEY (id);


--
-- Name: yard_images_base64 yard_images_base64_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_images_base64
    ADD CONSTRAINT yard_images_base64_pkey PRIMARY KEY (id);


--
-- Name: yard_logo yard_logo_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_logo
    ADD CONSTRAINT yard_logo_pkey PRIMARY KEY (id);


--
-- Name: yard_selectcamera yard_selectcamera_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_selectcamera
    ADD CONSTRAINT yard_selectcamera_pkey PRIMARY KEY (id);


--
-- Name: yard_settings yard_settings_name_key; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_settings
    ADD CONSTRAINT yard_settings_name_key UNIQUE (name);


--
-- Name: yard_settings yard_settings_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_settings
    ADD CONSTRAINT yard_settings_pkey PRIMARY KEY (id);


--
-- Name: yard_supplier yard_supplier_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_supplier
    ADD CONSTRAINT yard_supplier_pkey PRIMARY KEY (id);


--
-- Name: yard_supplier yard_supplier_supplier_name_key; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_supplier
    ADD CONSTRAINT yard_supplier_supplier_name_key UNIQUE (supplier_name);


--
-- Name: yard_transaction yard_transaction_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_transaction
    ADD CONSTRAINT yard_transaction_pkey PRIMARY KEY (id);


--
-- Name: yard_user yard_user_email_key; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user
    ADD CONSTRAINT yard_user_email_key UNIQUE (email);


--
-- Name: yard_user_groups yard_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user_groups
    ADD CONSTRAINT yard_user_groups_pkey PRIMARY KEY (id);


--
-- Name: yard_user_groups yard_user_groups_user_id_group_id_211b4c4e_uniq; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user_groups
    ADD CONSTRAINT yard_user_groups_user_id_group_id_211b4c4e_uniq UNIQUE (user_id, group_id);


--
-- Name: yard_user yard_user_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user
    ADD CONSTRAINT yard_user_pkey PRIMARY KEY (id);


--
-- Name: yard_user_user_permissions yard_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user_user_permissions
    ADD CONSTRAINT yard_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: yard_user_user_permissions yard_user_user_permissions_user_id_permission_id_5f0d112a_uniq; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user_user_permissions
    ADD CONSTRAINT yard_user_user_permissions_user_id_permission_id_5f0d112a_uniq UNIQUE (user_id, permission_id);


--
-- Name: yard_vehicle yard_vehicle_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_vehicle
    ADD CONSTRAINT yard_vehicle_pkey PRIMARY KEY (id);


--
-- Name: yard_warehouse yard_warehouse_name_key; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_warehouse
    ADD CONSTRAINT yard_warehouse_name_key UNIQUE (name);


--
-- Name: yard_warehouse yard_warehouse_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_warehouse
    ADD CONSTRAINT yard_warehouse_pkey PRIMARY KEY (id);


--
-- Name: yard_yard_list yard_yard_list_name_key; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_yard_list
    ADD CONSTRAINT yard_yard_list_name_key UNIQUE (name);


--
-- Name: yard_yard_list yard_yard_list_pkey; Type: CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_yard_list
    ADD CONSTRAINT yard_yard_list_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: scale_app_devices_name_a1cace4c_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX scale_app_devices_name_a1cace4c_like ON public.scale_app_devices USING btree (name varchar_pattern_ops);


--
-- Name: scale_app_transaction_device_id_bf976688; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX scale_app_transaction_device_id_bf976688 ON public.scale_app_transaction USING btree (device_id);


--
-- Name: yard_article_meta_article_id_742c60ec; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_article_meta_article_id_742c60ec ON public.yard_article_meta USING btree (article_id);


--
-- Name: yard_article_meta_yard_id_004f01bf; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_article_meta_yard_id_004f01bf ON public.yard_article_meta USING btree (yard_id);


--
-- Name: yard_article_supplier_id_42a19966; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_article_supplier_id_42a19966 ON public.yard_article USING btree (supplier_id);


--
-- Name: yard_article_ware_house_id_6872f764; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_article_ware_house_id_6872f764 ON public.yard_article USING btree (ware_house_id);


--
-- Name: yard_article_yard_id_6a63db80; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_article_yard_id_6a63db80 ON public.yard_article USING btree (yard_id);


--
-- Name: yard_combination_article_id_cf35364a; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_combination_article_id_cf35364a ON public.yard_combination USING btree (article_id);


--
-- Name: yard_combination_building_site_id_31b8603f; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_combination_building_site_id_31b8603f ON public.yard_combination USING btree (building_site_id);


--
-- Name: yard_combination_customer_id_0d9ba8f8; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_combination_customer_id_0d9ba8f8 ON public.yard_combination USING btree (customer_id);


--
-- Name: yard_combination_forwarders_id_96a62c63; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_combination_forwarders_id_96a62c63 ON public.yard_combination USING btree (forwarders_id);


--
-- Name: yard_combination_ident_dd507c80_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_combination_ident_dd507c80_like ON public.yard_combination USING btree (ident varchar_pattern_ops);


--
-- Name: yard_combination_supplier_id_122dfd7b; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_combination_supplier_id_122dfd7b ON public.yard_combination USING btree (supplier_id);


--
-- Name: yard_combination_vehicle_id_707c33e3; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_combination_vehicle_id_707c33e3 ON public.yard_combination USING btree (vehicle_id);


--
-- Name: yard_combination_yard_id_3c614565; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_combination_yard_id_3c614565 ON public.yard_combination USING btree (yard_id);


--
-- Name: yard_container_last_site_id_850dfddf; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_container_last_site_id_850dfddf ON public.yard_container USING btree (last_site_id);


--
-- Name: yard_container_name_8454f58d_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_container_name_8454f58d_like ON public.yard_container USING btree (name varchar_pattern_ops);


--
-- Name: yard_customer_name_af536799_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_customer_name_af536799_like ON public.yard_customer USING btree (name varchar_pattern_ops);


--
-- Name: yard_customer_warehouse_id_3cfe9e0a; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_customer_warehouse_id_3cfe9e0a ON public.yard_customer USING btree (warehouse_id);


--
-- Name: yard_forwarders_name_5d36371c_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_forwarders_name_5d36371c_like ON public.yard_forwarders USING btree (name varchar_pattern_ops);


--
-- Name: yard_images_base64_transaction_id_75bda9d8; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_images_base64_transaction_id_75bda9d8 ON public.yard_images_base64 USING btree (transaction_id);


--
-- Name: yard_settings_name_c54ec768_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_settings_name_c54ec768_like ON public.yard_settings USING btree (name varchar_pattern_ops);


--
-- Name: yard_settings_yard_id_9c2994d4; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_settings_yard_id_9c2994d4 ON public.yard_settings USING btree (yard_id);


--
-- Name: yard_supplier_supplier_name_533a4286_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_supplier_supplier_name_533a4286_like ON public.yard_supplier USING btree (supplier_name varchar_pattern_ops);


--
-- Name: yard_supplier_warehouse_id_75e7d162; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_supplier_warehouse_id_75e7d162 ON public.yard_supplier USING btree (warehouse_id);


--
-- Name: yard_transaction_article_id_10b0c55e; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_transaction_article_id_10b0c55e ON public.yard_transaction USING btree (article_id);


--
-- Name: yard_transaction_customer_id_be6fe566; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_transaction_customer_id_be6fe566 ON public.yard_transaction USING btree (customer_id);


--
-- Name: yard_transaction_supplier_id_96d41e88; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_transaction_supplier_id_96d41e88 ON public.yard_transaction USING btree (supplier_id);


--
-- Name: yard_transaction_vehicle_id_0452d9e4; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_transaction_vehicle_id_0452d9e4 ON public.yard_transaction USING btree (vehicle_id);


--
-- Name: yard_transaction_yard_id_d04d9761; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_transaction_yard_id_d04d9761 ON public.yard_transaction USING btree (yard_id);


--
-- Name: yard_user_email_a63a80cb_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_user_email_a63a80cb_like ON public.yard_user USING btree (email varchar_pattern_ops);


--
-- Name: yard_user_groups_group_id_02dc603a; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_user_groups_group_id_02dc603a ON public.yard_user_groups USING btree (group_id);


--
-- Name: yard_user_groups_user_id_71cb25fa; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_user_groups_user_id_71cb25fa ON public.yard_user_groups USING btree (user_id);


--
-- Name: yard_user_user_permissions_permission_id_a94149d3; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_user_user_permissions_permission_id_a94149d3 ON public.yard_user_user_permissions USING btree (permission_id);


--
-- Name: yard_user_user_permissions_user_id_c99c02b9; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_user_user_permissions_user_id_c99c02b9 ON public.yard_user_user_permissions USING btree (user_id);


--
-- Name: yard_user_yard_id_618964e2; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_user_yard_id_618964e2 ON public.yard_user USING btree (yard_id);


--
-- Name: yard_vehicle_forwarder_id_cf6b0b0d; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_vehicle_forwarder_id_cf6b0b0d ON public.yard_vehicle USING btree (forwarder_id);


--
-- Name: yard_warehouse_name_01d872a7_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_warehouse_name_01d872a7_like ON public.yard_warehouse USING btree (name varchar_pattern_ops);


--
-- Name: yard_yard_list_name_5344ed7f_like; Type: INDEX; Schema: public; Owner: yardman_admin
--

CREATE INDEX yard_yard_list_name_5344ed7f_like ON public.yard_yard_list USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_yard_user_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_yard_user_id FOREIGN KEY (user_id) REFERENCES public.yard_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: scale_app_transaction scale_app_transactio_device_id_bf976688_fk_scale_app; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.scale_app_transaction
    ADD CONSTRAINT scale_app_transactio_device_id_bf976688_fk_scale_app FOREIGN KEY (device_id) REFERENCES public.scale_app_devices(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_article_meta yard_article_meta_article_id_742c60ec_fk_yard_article_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_article_meta
    ADD CONSTRAINT yard_article_meta_article_id_742c60ec_fk_yard_article_id FOREIGN KEY (article_id) REFERENCES public.yard_article(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_article_meta yard_article_meta_yard_id_004f01bf_fk_yard_yard_list_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_article_meta
    ADD CONSTRAINT yard_article_meta_yard_id_004f01bf_fk_yard_yard_list_id FOREIGN KEY (yard_id) REFERENCES public.yard_yard_list(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_article yard_article_supplier_id_42a19966_fk_yard_supplier_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_article
    ADD CONSTRAINT yard_article_supplier_id_42a19966_fk_yard_supplier_id FOREIGN KEY (supplier_id) REFERENCES public.yard_supplier(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_article yard_article_ware_house_id_6872f764_fk_yard_warehouse_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_article
    ADD CONSTRAINT yard_article_ware_house_id_6872f764_fk_yard_warehouse_id FOREIGN KEY (ware_house_id) REFERENCES public.yard_warehouse(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_article yard_article_yard_id_6a63db80_fk_yard_yard_list_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_article
    ADD CONSTRAINT yard_article_yard_id_6a63db80_fk_yard_yard_list_id FOREIGN KEY (yard_id) REFERENCES public.yard_yard_list(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_combination yard_combination_article_id_cf35364a_fk_yard_article_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_combination
    ADD CONSTRAINT yard_combination_article_id_cf35364a_fk_yard_article_id FOREIGN KEY (article_id) REFERENCES public.yard_article(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_combination yard_combination_building_site_id_31b8603f_fk_yard_buil; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_combination
    ADD CONSTRAINT yard_combination_building_site_id_31b8603f_fk_yard_buil FOREIGN KEY (building_site_id) REFERENCES public.yard_buildingsite(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_combination yard_combination_customer_id_0d9ba8f8_fk_yard_customer_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_combination
    ADD CONSTRAINT yard_combination_customer_id_0d9ba8f8_fk_yard_customer_id FOREIGN KEY (customer_id) REFERENCES public.yard_customer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_combination yard_combination_forwarders_id_96a62c63_fk_yard_forwarders_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_combination
    ADD CONSTRAINT yard_combination_forwarders_id_96a62c63_fk_yard_forwarders_id FOREIGN KEY (forwarders_id) REFERENCES public.yard_forwarders(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_combination yard_combination_supplier_id_122dfd7b_fk_yard_supplier_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_combination
    ADD CONSTRAINT yard_combination_supplier_id_122dfd7b_fk_yard_supplier_id FOREIGN KEY (supplier_id) REFERENCES public.yard_supplier(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_combination yard_combination_vehicle_id_707c33e3_fk_yard_vehicle_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_combination
    ADD CONSTRAINT yard_combination_vehicle_id_707c33e3_fk_yard_vehicle_id FOREIGN KEY (vehicle_id) REFERENCES public.yard_vehicle(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_combination yard_combination_yard_id_3c614565_fk_yard_yard_list_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_combination
    ADD CONSTRAINT yard_combination_yard_id_3c614565_fk_yard_yard_list_id FOREIGN KEY (yard_id) REFERENCES public.yard_yard_list(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_container yard_container_last_site_id_850dfddf_fk_yard_buildingsite_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_container
    ADD CONSTRAINT yard_container_last_site_id_850dfddf_fk_yard_buildingsite_id FOREIGN KEY (last_site_id) REFERENCES public.yard_buildingsite(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_customer yard_customer_warehouse_id_3cfe9e0a_fk_yard_warehouse_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_customer
    ADD CONSTRAINT yard_customer_warehouse_id_3cfe9e0a_fk_yard_warehouse_id FOREIGN KEY (warehouse_id) REFERENCES public.yard_warehouse(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_images_base64 yard_images_base64_transaction_id_75bda9d8_fk_yard_tran; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_images_base64
    ADD CONSTRAINT yard_images_base64_transaction_id_75bda9d8_fk_yard_tran FOREIGN KEY (transaction_id) REFERENCES public.yard_transaction(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_settings yard_settings_yard_id_9c2994d4_fk_yard_yard_list_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_settings
    ADD CONSTRAINT yard_settings_yard_id_9c2994d4_fk_yard_yard_list_id FOREIGN KEY (yard_id) REFERENCES public.yard_yard_list(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_supplier yard_supplier_warehouse_id_75e7d162_fk_yard_warehouse_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_supplier
    ADD CONSTRAINT yard_supplier_warehouse_id_75e7d162_fk_yard_warehouse_id FOREIGN KEY (warehouse_id) REFERENCES public.yard_warehouse(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_transaction yard_transaction_article_id_10b0c55e_fk_yard_article_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_transaction
    ADD CONSTRAINT yard_transaction_article_id_10b0c55e_fk_yard_article_id FOREIGN KEY (article_id) REFERENCES public.yard_article(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_transaction yard_transaction_customer_id_be6fe566_fk_yard_customer_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_transaction
    ADD CONSTRAINT yard_transaction_customer_id_be6fe566_fk_yard_customer_id FOREIGN KEY (customer_id) REFERENCES public.yard_customer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_transaction yard_transaction_supplier_id_96d41e88_fk_yard_supplier_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_transaction
    ADD CONSTRAINT yard_transaction_supplier_id_96d41e88_fk_yard_supplier_id FOREIGN KEY (supplier_id) REFERENCES public.yard_supplier(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_transaction yard_transaction_vehicle_id_0452d9e4_fk_yard_vehicle_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_transaction
    ADD CONSTRAINT yard_transaction_vehicle_id_0452d9e4_fk_yard_vehicle_id FOREIGN KEY (vehicle_id) REFERENCES public.yard_vehicle(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_transaction yard_transaction_yard_id_d04d9761_fk_yard_yard_list_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_transaction
    ADD CONSTRAINT yard_transaction_yard_id_d04d9761_fk_yard_yard_list_id FOREIGN KEY (yard_id) REFERENCES public.yard_yard_list(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_user_groups yard_user_groups_group_id_02dc603a_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user_groups
    ADD CONSTRAINT yard_user_groups_group_id_02dc603a_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_user_groups yard_user_groups_user_id_71cb25fa_fk_yard_user_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user_groups
    ADD CONSTRAINT yard_user_groups_user_id_71cb25fa_fk_yard_user_id FOREIGN KEY (user_id) REFERENCES public.yard_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_user_user_permissions yard_user_user_permi_permission_id_a94149d3_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user_user_permissions
    ADD CONSTRAINT yard_user_user_permi_permission_id_a94149d3_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_user_user_permissions yard_user_user_permissions_user_id_c99c02b9_fk_yard_user_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user_user_permissions
    ADD CONSTRAINT yard_user_user_permissions_user_id_c99c02b9_fk_yard_user_id FOREIGN KEY (user_id) REFERENCES public.yard_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_user yard_user_yard_id_618964e2_fk_yard_yard_list_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_user
    ADD CONSTRAINT yard_user_yard_id_618964e2_fk_yard_yard_list_id FOREIGN KEY (yard_id) REFERENCES public.yard_yard_list(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: yard_vehicle yard_vehicle_forwarder_id_cf6b0b0d_fk_yard_forwarders_id; Type: FK CONSTRAINT; Schema: public; Owner: yardman_admin
--

ALTER TABLE ONLY public.yard_vehicle
    ADD CONSTRAINT yard_vehicle_forwarder_id_cf6b0b0d_fk_yard_forwarders_id FOREIGN KEY (forwarder_id) REFERENCES public.yard_forwarders(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

